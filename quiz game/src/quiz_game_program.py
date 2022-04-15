#imports Objects and lists
from question_bank_data import question_bank
from Multiple_Choice import MC_Quiz
""" 
Purpose of the quiz game
The game allows the user to play a quiz game. They will be given 5 multiple choice questions to answer.
If the player can guess all of the questions correctly they will win a secret joke at the end of the game. 
The player can play as many times as they want. So they have as many chances to get the secret joke. 
"""
#import imports
import time
import os
os.system('clear')
print("Welcome to my python quiz game! \n\nIn this game you will be given a question and its multiple choice answers \n"
        "Select the answer you think that fits and if you are correct you will score a point! \n" 
        "At the end of the game you will be given a score of how well you did and if you unlocked the secret joke! \n"
)
playing = input("Do you want to play? (Yes or no) \n")

#checks to make sure that the user enters in only letters
while True:
    if playing.isalpha():
        break
    else:
        print("Must answer yes or no")
        #used to delay prints to simulate a game featured
        time.sleep(2)
        playing = input("Do you want to play? (yes or no) \n")
        continue

#double checks that the user only enters yes or no
while (playing != "yes" and playing != "no"):
    print("Please enter yes or no")
    time.sleep(2)
    playing = input("Do you want to play? (Yes or no)" + "\n")
    if playing.lower() =="yes":
        break
    else:
        continue

#Quits the game if they don't want to play
if playing.lower() =="no":
    os.system('clear')
    print("Why did you come here?")
    quit()

#starts keeping score of the game
#keeps track of idk scores
os.system('clear')
print("Awesome lets get started!!! \n")
time.sleep(2)

#stores the question and their answers in objects
#creates the list
questions = []
#adds to the list
questions.append(MC_Quiz(question_bank[0], "B"))
questions.append(MC_Quiz(question_bank[1], "D"))
questions.append(MC_Quiz(question_bank[2], "C"))
questions.append(MC_Quiz(question_bank[3], "B"))
questions.append(MC_Quiz(question_bank[4], "A"))


stop_playing = "no"   #phrase used for ending the game
continue_playing = "yes" #phrase for continuing to play
end_of_game = ""      #initializes the end game code 

#starts the game in a psuedo do while loop
while True:
    score = 0 #keeps score of the game and resets the score when teh loop starts again
    for current_question in questions:
        answer = input(current_question.prompt) 
        if answer.isalpha():
            #if they guess correctly 
            if current_question.answer == answer.upper():
                os.system('clear')
                print("Thats correct! \n")
                score += 1
                print("Current score " + str(score) + "\n")
            #if they guess incorrectly
            else:
                os.system('clear')
                print("Darn that was not teh correct answer \n\n" + "The correct answer was: " + current_question.answer + "\n\n")
                print("Current score " + str(score) + "\n")
        #if they enter anything other than a number
        else:
            print("Incorrect please enter a leeter \n")
            print("Current score " + str(score) + "\n")
        #Grading of the quiz 
        #if they guess all of the correct answers
    if score == 5:
            os.system('clear')
            print("You got all the questions correct!!!" + "\n")
            time.sleep(2)
            print("Since you did so well here is one more dad joke" + "\n")
            time.sleep(2)
            print("What do you call a busy waiter? A server! XD" + "\n") 
            time.sleep(2)
            print("Thank you for playing!!!")
    #if they didn't guess all the correct answers
    elif (score < 5):
        os.system('clear')
        print("Darn you didn't get all the questions correct :/ " + "\n")
        time.sleep(2)
        print("Go back and try to get all the answers correct! Theres a secret!!!"+ "\n")
        time.sleep(2)
        print("Thank you for playing!!" + "\n")
#prompts the user if they want to play again then cycles back to the top of the while loop
    end_of_game = input("do you want to play again? (yes or no)" + "\n")
    if end_of_game.lower() == stop_playing:
        quit()
    elif end_of_game.lower() == continue_playing:
        continue
    while (end_of_game != "yes" and end_of_game != "no"):
        print("Please enter yes or no")
        time.sleep(2)
        playing = input("Do you want to play? (Yes or no)" + "\n")
        if playing.lower() =="yes":
            break
        else:
            continue
