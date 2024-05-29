# CSE 310 - Module Report

Name:Bryce Chesley

## Part 1 - Module Planning

This section should be filled on the first Monday of the Sprint and submitted

### Section 1.1 - Module Selection

1. What Sprint is this for (1-5)?
sprint 2

2. Select the Module (with a single X) that you will do this Sprint:

|Module                   |Selected Module|
|-------------------------|---------------|
|Cloud Databases          |               |
|Data Analysis            |               |
|Game Framework           |        X      |
|GIS Mapping              |               |
|Mobile App               |               |
|Networking               |               |
|SQL Relational Databases |               |
|Web Apps                 |               |
|C++                      |               |
|Java                     |               |
|Kotlin                   |               |
|Erlang                   |               |
|TypeScript               |               |
|Rust                     |               |
|Choose Your Own Adventure|               |

3. Find the list of unique requirements for your selected module in the Module Summary in Canvas.  In some circumstances, you will need to modify the requirements based on the technology or language you selected.  For the Choose Your Own Adventure, you need to create your own requirements.  List the unique module requirements below:
Write a simple game using any game framework such as PyGame, Arcade (Python), Unity, or GoDot. You can also create your own by using graphics packages like OpenGL or Raylib.

The game must have the following characteristics:

The game must display graphics

The game must take user input from the keyboard or mouse

The game must have moveable objects

Stretch Challenges (select one):

Allow the user to save and load the game.

Add music or sound effects to the game.

Provide levels in your game that change the difficulty of the game.

### Section 1.2 - Planning

During the Sprint, you will spend 4 hours in class meetings, 4 hours on your team project (2 of which during class), and 10 hours on your selected module.  Make a plan for your 10 hours by answering the questions below.  You should refer back to this plan and make adjustments during the Sprint.

1. What sources have you selected to learn the technical material?
https://api.arcade.academy/en/latest/examples/index.html
chatgpt

2. What is your plan to practice the new material?  In other words, what is the order in which you plan to learn the material before working on your demonstration software?
First ill get it to display somthing, then move, then add more intracacy after that.

3. What demonstration software do you plan on submitting at the end of the Sprint (note that this can and may change)?
a top down 2d dungeon crawler

4. Identify the days, times, and locations that you will work on the module.
probably moday/wednesdays for about an hour at a time.

5. Identify both a technical risk and a behavioral risk that you antcipate may occur during this Sprint.  What is your mitgigation plan?
I have used python beofre but not pygame, so hopefully i can wrap my head around it.


## Part 2 - Time Log

This section should be filled out during the Sprint. 

Record all CSE 310 work that you do on your individual module or the team project.  Include time learning, practicing, developing, testing, and documenting.  Don't include time spent in the 4 class meetings (Planning, Stand-Up, Team Review, and Individual Review).  You will need to sum of these hours at the end of the Sprint. Note that the hours you report will affect your grades.

Note that `IM` stands for Individual Module and `TP` stands for Team Project.  

|Date      |Start Time|IM or TP|Description                                 |Hours:Minutes|
|----------|----------|--------|--------------------------------------------|-------------|
| 05/15/24 |   4:00   |    IM  | getting pygame working and installed       |    2:00     |
| 05/18/24 |   4:00   |    TP  | figuring out django a little bit           |    2:00     |
| 05/20/24 |   4:00   |    IM  |getting the game fully up to what i want    |    6:00     |
| 05/22/24 |   6:00   |    TP  |team meeting where we found a hosting service|   2:00     |
| 05/23/24 |   9:00   |    IM  |bug fixing, adding features and randomness  |    3:00     |
|          |          |        |                                            |             |

_Note: Add more rows as needed._


## Part 3 - Module Results

This section should be filled out at the end of the Sprint and submitted.

1. Put your GitHub link for your demonstration software here: https://github.com/brycches/Applied_programing/tree/master/week%204

2. Put your YouTube link for your code walkthrough and demo video here: https://youtu.be/zvSTMEEJCy8

3. Complete the following checklist by either indicating "Yes" or "No". If you indicate "No" then provide an explanation of why beneath the table.

|Question                                                    |Response|
|------------------------------------------------------------|--------|
|Are the links above public and working?                     |    Y   |
|Did you complete all the unique requirements for the module?|    Y   |
|Did you write at least 100 lines of code?                   |    Y   |
|Did you fully complete the readme.md file?                  |    Y   |
|Did you put the readme.md file in GitHub in the top folder? |    Y   |

4. If you completed a Stretch Challenge (as shown in the Module Description document in Canvas) then describe what you did.  If you did the Choose Your Own Adventure module, then you get to decide what qualifies as a Stretch Challenge. I added a difficulty system, in that if you find the stairs down event it will generate a whole new dungeon.

5. Did you change your selected module during the middle of the Sprint?  If yes, then describe what you changed it to, when you changed it, and why you changed it. no

6. Using the log above, fill in the total hours and minutes you spent on the individual module:

|Activity         |Total Hours:Minutes|
|-----------------|-------------------|
|Individual Module|        11         |

7. What strategies (behavioral and technical) worked well during this Sprint?  What did not work well?  List some possible ways that you can improve next Sprint.
Everything worked well, i just need to do better at turning this portion of the sprint in on time.





        instructions_text1 = font.render("Use UP/DOWN to select a stat,", True, WHITE)
        instructions_text2 = font.render("LEFT/RIGHT to allocate points,", True, WHITE)
        instructions_text3 = font.render("ENTER to start", True, WHITE)
        screen.blit(instructions_text1, (50, 400))
        screen.blit(instructions_text2, (50, 450))
        screen.blit(instructions_text3, (50, 500))