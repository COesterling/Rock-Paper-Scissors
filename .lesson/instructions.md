# Project 2: Rock Paper Scissors Spin-Off Game

## Learning Outcomes:

* Use and call functions
* Call a function with a parameter
* Import the random module
* Use if/else if/else statements to determine the flow of the program
* Comment your code
* Debug your code
* Test your code

## Scenario

You will build a Rock-Paper-Scissors type of game, but with your own three items. The user will play against your computer program player and you will keep track of the scores. 

### Some suggestions for items:

* Elemental - fire, water, wind
* Marvel characters battle - Iron Man, Captain America, Thor
* Cooking themed - microwave, toaster, fire pit
* Animal themed - cats, dogs, hamsters
be creative and have fun!

### The program must do the following: 

* Print out a title for the game.
* Ask the user their name.
* Greet the user.
* Ask if they would like to play a game.
* If yes, continue to the game.
* If no, print a farewell message and exit the game.

## Playing the game

* Print out instructions on how to play the game. 
* Describe the items and whether the items will win or lose compared to the other items. 
  * Format the instructions nicely for the best user experience.
* Generate a random Computer Player name using two lists. 
  * One will be the first part of the name, and the other will be the second part of the name. 
  * Have at least 5 items in each list to generate a username made from both lists.
* Ask the user which choice they would like to select.
* Randomly pick a choice for the Computer Player. 
  * Hint: You might want to generate a random number from 1 to 3, and then do an if statement that will align the random number to a particular option. Or you can use a list and pick the index of the choice. 1 might be rock, 2 might be paper, and 3 might be scissors.                 
* Compare the choices for a win, loss or tie. 
* Record each players stats. 
* Output the stats at the end of each game. 
* Ask the player if they would like to play again.
  * If so, start the process again, keeping the stats updated with the correct values.

## Technical Requirements

* Import and use the random module.
* Use at least TWO functions.
  * One function must pass a parameter. 
  * One function must return a value.
* Use if/elif/else to help control program flow.
* Be aware of the user experience. 

## For advanced coders/challenge

If you want an extra challenge, modify the scenario above with more than 3 options. Ex: Rock, Paper, Scissors, and Fire.

## Tips

* Create pseudocode for your program - natural language for the steps you would like to do to meet the assignment requirements. 
* Start with the requirements as comments in your program and continue from there.
* Do one thing at a time. Code. Test. Code. Test. If you look at this program in tiny bite sizes then it is less overwhelming.
* Think about what parts of the program are repetitive that can easily be put into a function. play_game()? game_menu()? What else?
* Have fun and be creative. This can be a really exciting program to build. 