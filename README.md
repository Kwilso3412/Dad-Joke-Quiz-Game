# OOP quiz game
This project creates a game that will allow the user to play a game in the console for as long as they want until they exit the game.

By using a combination of time.sleep() function, which causes the code to take a brief pause, and clearing the console. I recreated a game that will allow the user to read each line one at a time.. This effect recreated how text was displayed in an old RPG like Final Fantasy on the NES. 

Python does not have a built in do-while loop as other higher-level languages, so I created a pseudo-do-while loop. The major program is on one large while loop and the game is ended when the player enters the end game phrase. 

The last aspect of the game is if the user can guess all the correct answers, they are given a reward. Otherwise they are told.

****NOTE****

Depending on your operating system, you will need to change the console clear code. If you are using a windows machine, you will need to use os.system(‘cls’). If you are using macOS or Linux, you will need to use os.system(‘clear’).

