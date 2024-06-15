function fetchPokemonData() {
    const inputElement = document.getElementById('pokemonName');
    let pokemonName = inputElement.value.toLowerCase();

    // Check if the input is empty, and provide a default value if it is
    if (pokemonName === '') {
        pokemonName = 'pikachu'; // You can set any default name you prefer
        inputElement.value = pokemonName; // Update the input field to show the default name
    }

    const apiUrl = `https://pokeapi.co/api/v2/pokemon/${pokemonName}/`;

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Pokemon not found: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            fetchPokemonTypeData(data.types);
        })
        .catch(error => {
            displayError(error);
        });
}

function fetchPokemonTypeData(types) {
    const typePromises = types.map(type => fetch(type.type.url)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Type data not found: ${response.status}`);
            }
            //console.log(response);
            return response.json();
        }));

    Promise.all(typePromises)
        .then(typeData => {
            const weaknesses = typeData.reduce((acc, typeInfo) => {
                const weaknessTypes = typeInfo.damage_relations.double_damage_from.map(weakness => weakness.name);
                console.log('weakness types without calling type effectiveness', weaknessTypes);
                return acc.concat(weaknessTypes);
            }, []);
            console.log(weaknesses);

            displayPokemonWeaknesses(weaknesses);
        })
        .catch(error => {
            displayError(error);
        });
}

function fetchMoveData(moveUrl) {
    return fetch(moveUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Move data not found: ${response.status}`);
            }
            return response.json();
        });
}

function displayPokemonWeaknesses(weaknesses) {
    const resultElement = document.getElementById('result');
    resultElement.innerHTML = '';

    resultElement.innerHTML += `<h2>Defensive Weaknesses: ${Array.from(new Set(weaknesses)).join(', ')}</h2>`;

    const pokemonData = fetchPokemonDataByName(document.getElementById('pokemonName').value.toLowerCase())
        .then(data => {
            const moves = data.moves.map(move => move.move);

            const movePromises = moves.map(move => {
                //console.log('move.url', move.url)
                return fetchMoveData(move.url)
                    .then(moveData => {
                        const moveType = moveData.type.name;
                        const damageClass = moveData.damage_class.name;
                        const power = moveData.power;
                        const accuracy = moveData.accuracy;
                        const effectEntries = moveData.effect_entries;
                        const moveName = move.name;

                        // Determine effectiveness against each type
                        const effectiveness = determineEffectiveness(moveType);

                        return {
                            move: moveName,
                            type: moveType,
                            damageClass,
                            power,
                            accuracy,
                            effectEntries,
                            effectiveness,
                        };
                    });
            });

            Promise.all(movePromises)
                .then(moveInfoList => {
                    moveInfoList.forEach(moveInfo => {
                        resultElement.innerHTML += `<h3>Move: ${moveInfo.move}</h3>`;
                        resultElement.innerHTML += `<p>Type: ${moveInfo.type}</p>`;
                        resultElement.innerHTML += `<p>Damage Class: ${moveInfo.damageClass}</p>`;
                        resultElement.innerHTML += `<p>Power: ${moveInfo.power || 'N/A'}</p>`;
                        resultElement.innerHTML += `<p>Accuracy: ${moveInfo.accuracy || 'N/A'}</p>`;

                        // Check if effectEntries is not empty before accessing short_effect
                        if (moveInfo.effectEntries.length > 0) {
                            resultElement.innerHTML += `<p>Effect: ${moveInfo.effectEntries[0].short_effect || 'N/A'}</p>`;
                        } else {
                            resultElement.innerHTML += `<p>Effect: N/A</p>`;
                        }
                        
                        resultElement.innerHTML += `<p>${determineEffectiveness(moveInfo.type)}</p>`
                        resultElement.innerHTML += `<hr>`;
                    });
                })
                .catch(error => {
                    displayError(error);
                });
        });
    //console.log(pokemonData)
}


function determineEffectiveness(moveType) {
    console.log(moveType)
    
    const effectivenessAgainstAllTypes = getTypeEffectiveness(moveType);
    sentence = ''
    for (const targetType in effectivenessAgainstAllTypes) {
        if (effectivenessAgainstAllTypes[targetType] === 1)
        {
         sentence += `<div>${effectivenessAgainstAllTypes[targetType]}x vs ${targetType}</div>`;
        }
        else if (effectivenessAgainstAllTypes[targetType] === 2)
        {
            sentence += `<div> <span style="background-color: green; color: white">${effectivenessAgainstAllTypes[targetType]}x vs ${targetType}</span></div>`;
        }
        else if (effectivenessAgainstAllTypes[targetType] === 0.5)
        {
            sentence += `<div> <span style="background-color: red;">${effectivenessAgainstAllTypes[targetType]}x vs ${targetType}</span></div>`;
        }
        else if (effectivenessAgainstAllTypes[targetType] === 0)
        {
            sentence += `<div> <span style="color: white; background-color: black">${effectivenessAgainstAllTypes[targetType]}x vs ${targetType}</span></div>`;
;
        }
    }
    console.log(sentence)
    return sentence
}


function getTypeEffectiveness(moveType) {
    // Your type effectiveness values here...
    const typeEffectivenessValues = {
        normal: {
            bug: 1, dark: 1, dragon: 1, electric: 1, fairy: 1, fighting: 1, fire: 1, flying: 1, ghost: 0, grass: 1, ground: 1, ice: 1, normal: 1, poison: 1, psychic: 1, rock: .5, steel: 0.5, water: 1
        },
        fire: {
            bug: 2, dark: 1, dragon: .5, electric: 1, fairy: 1, fighting: 1, fire: 0.5, flying: 1, ghost: 1, grass: 2, ground: 2, ice: 2, normal: 1, poison: 1, psychic: 1, rock: 0.5, steel: 2, water: 0.5
        },
        water: {
            bug: 1, dark: 1, dragon: .5, electric: 1, fairy: 1, fighting: 1, fire: 2, flying: 1, ghost: 1, grass: 0.5, ground: 2, ice: 1, normal: 1, poison: 1, psychic: 1, rock: 2, steel: 1, water: 0.5
        },
        electric: {
            bug: 0.5, dark: 1, dragon: 0.5, electric: 0.5, fairy: 1, fighting: 1, fire: 1, flying: 2, ghost: 1, grass: 0.5, ground: 0, ice: 1, normal: 1, poison: 1, psychic: 1, rock: 1, steel: 1, water: 2
        },
        grass: {
            bug: 2, dark: 1, dragon: 1, electric: 1, fairy: 1, fighting: 1, fire: 0.5, flying: 0.5, ghost: 1, grass: 0.5, ground: 2, ice: 1, normal: 1, poison: 0.5, psychic: 1, rock: 2, steel: 0.5, water: 2 
        },
        ice: {
            bug: 1, dark: 1, dragon: 2, electric: 1, fairy: 1, fighting: 1, fire: 0.5, flying: 2, ghost: 1, grass: 2, ground: 2, ice: 0.5, normal: 1, poison: 1, psychic: 1, rock: 1, steel: 0.5, water: 0.5
        },
        fighting: {
            bug: 0.5, dark: 2, dragon: 1, electric: 1, fairy: 0.5, fighting: 1, fire: 1, flying: 0.5, ghost: 0, grass: 1, ground: 1, ice: 2, normal: 2, poison: 0.5, psychic: 0.5, rock: 2, steel: 2, water: 1
        },
        poison: {
            bug: 0.5, dark: 1, dragon: 1, electric: 1, fairy: 2, fighting: 1, fire: 1, flying: 1, ghost: 0.5, grass: 2, ground: 0.5, ice: 1, normal: 1, poison: 0.5, psychic: 1, rock: 0.5, steel: 0, water: 1
        },
        ground: {
            bug: 0.5, dark: 1, dragon: 1, electric: 2, fairy: 1, fighting: 1, fire: 2, flying: 0, ghost: 1, grass: 0.5, ground: 1, ice: 1, normal: 1, poison: 2, psychic: 1, rock: 2, steel: 2, water: 1
        },
        flying: {
            bug: 2, dark: 1, dragon: 1, electric: 0.5, fairy: 1, fighting: 2, fire: 1, flying: 1, ghost: 1, grass: 2, ground: 1, ice: 1, normal: 1, poison: 1, psychic: 1, rock: 0.5, steel: 0.5, water: 1
        },
        psychic: {
            bug: 1, dark: 0, dragon: 1, electric: 1, fairy: 1, fighting: 2, fire: 1, flying: 1, ghost: 1, grass: 1, ground: 1, ice: 1, normal: 1, poison: 2, psychic: 0.5, rock: 1, steel: 0.5, water: 1
        },
        bug: {
            bug: 1, dark: 2, dragon: 1, electric: 1, fairy: 0.5, fighting: 0.5, fire: 0.5, flying: 0.5, ghost: 0.5, grass: 2, ground: 1, ice: 1, normal: 1, poison: 0.5, psychic: 2, rock: 1, steel: 0.5, water: 1
        },
        rock: {
            bug: 2, dark: 1, dragon: 1, electric: 1, fairy: 1, fighting: 0.5, fire: 2, flying: 2, ghost: 1, grass: 1, ground: 0.5, ice: 2, normal: 1, poison: 1, psychic: 1, rock: 1, steel: 0.5, water: 1
        },
        ghost: {
            bug: 1, dark: 0.5, dragon: 1, electric: 1, fairy: 1, fighting: 1, fire: 1, flying: 1, ghost: 2, grass: 1, ground: 1, ice: 1, normal: 0, poison: 1, psychic: 2, rock: 1, steel: 1, water: 1 
        },
        steel: {
            bug: 1, dark: 1, dragon: 1, electric: 0.5, fairy: 2, fighting: 1, fire: 0.5, flying: 1, ghost: 1, grass: 1, ground: 1, ice: 2, normal: 1, poison: 1, psychic: 1, rock: 2, steel: 0.5, water: 0.5
        },
        dragon: {
            bug: 1, dark: 1, dragon: 2, electric: 1, fairy: 0, fighting: 1, fire: 1, flying: 1, ghost: 1, grass: 1, ground: 1, ice: 1, normal: 1, poison: 1, psychic: 1, rock: 1, steel: 0.5, water: 1
        },
        dark: {
            bug: 1, dark: 0.5, dragon: 1, electric: 1, fairy: 0.5, fighting: 0.5, fire: 1, flying: 1, ghost: 2, grass: 1, ground: 1, ice: 1, normal: 1, poison: 1, psychic: 2, rock: 1, steel: 1, water: 1
        },
        fairy: {
            bug: 1, dark: 2, dragon: 2, electric: 1, fairy: 1, fighting: 2, fire: 0.5, flying: 1, ghost: 1, grass: 1, ground: 1, ice: 1, normal: 1, poison: 0.5, psychic: 1, rock: 1, steel: 0.5, water: 1
        },
    }

    const effectivenessAgainstAllTypes = {};
    counter = 0;
    for (const targetType in typeEffectivenessValues) {
        if (typeEffectivenessValues.hasOwnProperty(targetType)) {
            console.log('target type', targetType)
            console.log('move type', moveType)
            console.log('effectiveness against all types', typeEffectivenessValues[moveType][targetType] )
            effectivenessAgainstAllTypes[targetType] = typeEffectivenessValues[moveType][targetType];

            if (parseFloat(effectivenessAgainstAllTypes[targetType]) === 2)
            {
                effectivenessAgainstAllTypes[targetType] = 2
            }
            else if (parseFloat(effectivenessAgainstAllTypes[targetType]) === 0.5)
            {
                effectivenessAgainstAllTypes[targetType] = 0.5
            } 
            else if (parseFloat(effectivenessAgainstAllTypes[targetType]) === 0)
            {
                effectivenessAgainstAllTypes[targetType] = 0
            } 
            console.log('typeEffectivenessValues', typeEffectivenessValues)
            console.log('effectivenessAgainstAllTypes', effectivenessAgainstAllTypes)
            counter += 1
            console.log('counter', counter)
        }
    }
    console.log(effectivenessAgainstAllTypes);
    return effectivenessAgainstAllTypes;
}
function displayError(error) {
    const resultElement = document.getElementById('result');
    resultElement.innerHTML = `<p>Error: ${error.message}</p>`;
}

async function fetchPokemonDataByName(pokemonName) {
    const apiUrl = `https://pokeapi.co/api/v2/pokemon/${pokemonName}/`;
    const response = await fetch(apiUrl);
    if (!response.ok) {
        throw new Error(`Pokemon not found: ${response.status}`);
    }
    const data = await response.json();
    return data;
}

// Call this function with the initial value if you want to display information when the page loads.
fetchPokemonData();
