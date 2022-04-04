##purpose of this file is to create a program that will run the quiz game
from question_bank_data import question_bank
from quiz import Quiz_game
from quiz import Question

import time
import os, sys
#puts a delay in between prompts 
print("Welcome to My Quiz!! \n\n")
print("Welcome to my python quiz game! In this game you will be given a question and its multiple choice answers \n"
        "Select the answer you think that fits and if you are correct you will score a point! \n" 
        "At the end of the game you will be given a score of how well you did and if you unlocked the secret jok! \n"
    )
playing = input("Do you want to play? (Yes or no) \n")

#TODO create a main function that will house all the operations to the python program. 
#TODO randomize questions and incorporate for asking for hints
#TODO create a counter for how many wins and loses they user has earned 

#checks to make sure that the user enters in only letters
while True:
    if playing.isalpha():
        break
    else:
        os.system('clear')
        print("Must answer yes or no \n")
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
else:
    Score = 0
    idk_score = 0
os.system('clear')
print("Awesome lets get started!!!")
time.sleep(2)


end_game_phrase = "no"
continue_playing = "yes"

while True:
    #stores the question and their answers in objects
    questions = [
        Question(question_bank[0], "D"),
        Question(question_bank[1], "B"),
        Question(question_bank[2], "B"),
        Question(question_bank[3], "A"),
        Question(question_bank[4], "C"),
        Question(question_bank[5], "B"),
        Question(question_bank[6], "B"),
        Question(question_bank[7], "D"),
        Question(question_bank[8], "C"),
        Question(question_bank[9], "B"),
        Question(question_bank[10], "A"),
        Question(question_bank[11], "C"),
        ]

#Starts the Quiz game
    quiz = Quiz_game(questions)

    while quiz.remaining_questions():
        quiz.load_questions
        
    print("You've completed the quiz!!")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")


    #displays message for score and idk score
    # if Score == 3:
    #     os.system('cls')
    #     print("You got all the questions correct!!!" + "\n")
    #     time.sleep(2)
    #     print("Since you did so well here is one more dad joke" + "\n")
    #     time.sleep(2)
    #     print("What do you call a busy waiter? A server! XD" + "\n") 
    #     time.sleep(2)
    #     print("Thank you for playing!!!")

    # elif Score < 3 and idk_score <= 3:
    #     os.system('cls')
    #     print("Darn you didn't get all the questions correct :/ " + "\n")
    #     time.sleep(2)
    #     print("Go back and try to get all the answers correct! Theres a secret!!!"+ "\n")
    #     time.sleep(2)
    #     print("Thank you for playing!!")

    # #User should not see this but just in case there is something think of something when testing they will see this message
    # else:
    #     os.system('cls')
    #     print("How are you seeing this? Go back and play correctly!!" + "\n")


    # end_of_game = input("do you still want to play?" + "\n")

    # if end_of_game.lower() == end_game_phrase:
    #     quit()

    # elif end_of_game.lower() == continue_playing:
    #     continue

    # while (end_of_game != "yes" and end_of_game != "no"):
    #     print("Please enter yes or no")
    #     time.sleep(2)
    #     playing = input("Do you want to play? (Yes or no)" + "\n")
    #     if playing.lower() =="yes":
    #         break
    #     else:
    #         continue


