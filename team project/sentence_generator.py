import random

def get_determiner(quantity, word):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word_d = random.choice(words)
    if word_d == "a":
        vowels = 'aeiou'
        # Check the first letter of the word and determine if it's a vowel
        if word[0].lower() in vowels:
            return 'an'
        else:
            return 'a'
    return word_d

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = [
            "apple", "book", "clock", "desk", "elephant", "flower", "guitar", "house", "island", "jacket",
            "kite", "lamp", "mountain", "notebook", "orange", "pencil", "queen", "rose", "star", "tree",
            "umbrella", "vase", "window", "xylophone", "yacht", "zebra", "ball", "cloud", "door", "egg",
            "frog", "glass", "hat", "ice", "juice", "key", "leaf", "moon", "nest", "owl",
            "pear", "quilt", "ring", "sun", "teapot", "unicorn", "volcano", "whale", "x-ray", "yo-yo"
            ]
    else:
        words =  [
            "bottles", "chairs", "dishes", "engines", "forests", "grapes", "hills", "insects", "jungles", "knives",
            "lemons", "mirrors", "noodles", "oceans", "pizzas", "quizzes", "robots", "spoons", "tigers", "umbrellas",
            "valleys", "watches", "exhibits", "yarns", "zooms", "beans", "cups", "drums", "flutes", "gloves",
            "hearts", "islands", "jars", "kernels", "lanterns", "maps", "novels", "orbits", "peaches", "quests",
            "rivers", "shoes", "trains", "units", "villages", "wheels", "xenoliths", "years", "zeppelins", "winds"
            ]

    
    word_n = random.choice(words)
    return word_n

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """



    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote",
            "sang", "jumped", "listened", "worked", "played",
            "cried", "watched", "cooked", "met", "read",
            "drove", "bought", "wore", "broke", "chose",
            "drew", "drank", "fell", "forgot", "gave",
            "went", "knew", "made", "paid", "rode",
            "said", "saw", "sold", "sent", "stood",
            "won", "understood", "brought", "built", "caught",
            "cut", "found", "held", "kept", "let"]
    elif tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks",
                "runs", "sleeps", "talks", "walks", "writes",
                "sings", "jumps", "listens", "works", "plays",
                "cries", "watches", "cooks", "meets", "reads",
                "drives", "buys", "wears", "breaks", "chooses",
                "draws", "drinks", "falls", "forgets", "gives",
                "goes", "knows", "makes", "pays", "rides",
                "says", "sees", "sells", "sends", "stands",
                "wins", "understands", "brings", "builds", "catches",
                "cuts", "finds", "holds", "keeps", "lets"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think",
                "run", "sleep", "talk", "walk", "write",
                "sing", "jump", "listen", "work", "play",
                "cry", "watch", "cook", "meet", "read",
                "drive", "buy", "wear", "break", "choose",
                "draw", "drink", "fall", "forget", "give",
                "go", "know", "make", "pay", "ride",
                "say", "see", "sell", "send", "stand",
                "win", "understand", "bring", "build", "catch",
                "cut", "find", "hold", "keep", "let"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write", "will sing", "will jump",
            "will listen", "will work", "will play", "will cry",
            "will watch", "will cook", "will meet", "will read",
            "will drive", "will buy", "will wear", "will break",
            "will choose", "will draw", "will drink", "will fall",
            "will forget", "will give", "will go", "will know",
            "will make", "will pay", "will ride", "will say",
            "will see", "will sell", "will send", "will stand",
            "will win", "will understand", "will bring", "will build",
            "will catch", "will cut", "will find", "will hold",
            "will keep", "will let"]
    
    word_v = random.choice(words)
    return word_v

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """

    adjective = get_adjective()


    sentence = f" {get_prepositional_phrase(quantity).capitalize()}, {get_prepositional_phrase(quantity)}, {get_determiner(quantity, adjective)} {adjective} {get_noun(quantity)} {get_adverb()} {get_verb (quantity, tense)}"
    return sentence

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out of", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = [
        "above", "across", "against", "along", "amid", "among", "around", "at", "before", "behind",
        "below", "beneath", "beside", "between", "beyond", "by", "down", "during", "for", "from",
        "in", "inside", "into", "near", "off", "on", "onto", "out", "outside", "over",
        "past", "through", "to", "toward", "under", "until", "up", "within", "without", "across from",
        "next to", "opposite", "beside", "amongst", "against", "alongside", "upon", "aboard", "beyond", "about"
        ]
    word_p = random.choice(words)
    return word_p


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    if quantity == 1:
        noun = get_noun(1)
        preposition = get_preposition()
        adjective = get_adjective()
        determiner = get_determiner(1, adjective)
        phrase = (f"{preposition} {determiner} {adjective} {noun}")
        return phrase
    else:
        noun = get_noun(2)
        preposition = get_preposition()
        adjective = get_adjective()
        determiner = get_determiner(2, adjective)
        phrase = (f"{preposition} {determiner} {adjective} {noun}")
        return phrase

def get_adjective():
    """Return a randomly chosen adjective
    from this list of adjectives:
        "Beautiful", "Intelligent", "Courageous", "Creative", "Generous",
        "Compassionate", "Energetic", "Patient", "Joyful", "Loyal", "Reliable",
        "Humble", "Passionate", "Wise", "Resilient", "Honest", "Adventurous",
        "Gracious", "Determined", "Empathetic"

    Return: a randomly chosen adjective.
    """
    words = [
        "ancient", "beautiful", "cold", "dark", "elegant", "fragile", "gloomy", "heavy", "icy", "jolly",
        "kind", "large", "mysterious", "narrow", "old", "peaceful", "quiet", "rusty", "sunny", "tiny",
        "ugly", "vast", "wet", "xeric", "young", "zealous", "bright", "creaky", "dusty", "empty",
        "fuzzy", "golden", "hollow", "intricate", "juicy", "knotted", "luminous", "massive", "noisy", "ornate",
        "purple", "quaint", "ripe", "smooth", "thick", "velvety", "windy", "exotic", "yellow", "zippy"
        ]
    word_adj = random.choice(words)
    return word_adj

def get_adverb():
    """Return a randomly chosen adverb
    from this list of adverbs:
        "beautifully", "intelligently", "courageously", "creatively",
        "generously", "compassionately", "energetically", "patiently", "joyfully",
        "loyally", "reliably", "humbly", "passionately", "wisely","resiliently",
        "honestly", "adventurously", "graciously", "determinedly", "empathetically"

    Return: a randomly chosen adverb.
    """
    words = ["quickly", "slowly", "carefully", "easily", "quietly", "loudly", "happily", "sadly", "smoothly", "rapidly",
    "brightly", "darkly", "strongly", "gently", "suddenly", "usually", "frequently", "rarely", "never", "always",
    "completely", "partially", "almost", "absolutely", "together", "alone", "simply", "clearly", "obviously", "possibly",
    "probably", "actually", "eventually", "recently", "previously", "typically", "naturally", "certainly", "specifically", "directly",
    "equally", "greatly", "highly", "deeply", "barely", "hardly", "merely", "just", "only", "truly"]
    word_adv = random.choice(words)
    return word_adv




def main():
    length = int(input("how many sentances would you like to print "))
    tenses = ["past", "present", "future"]
    plural = [1,2]
    number = 0
    while number < length:
        sentance = make_sentence( random.choice(plural), random.choice(tenses))
        with open('output.txt', 'a') as file:
            file.write(f"{sentance}.\n")
        number += 1

main()
