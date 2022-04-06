#imports Objects and lists
from question_bank_data import question_bank
from quiz import Question

#import imports
import time
import os
import random
#puts a delay in between prompts 
print("Welcome to my python quiz game! \n\nIn this game you will be given a question and its multiple choice answers \n"
        "Select the answer you think that fits and if you are correct you will score a point! \n" 
        "At the end of the game you will be given a score of how well you did and if you unlocked the secret joke! \n"
)
playing = input("Do you want to play? (Yes or no) \n")

#TODO create a main function that will house all the operations to the python program. 
#TODO randomize questions and incorporate for asking for hints
#TODO create a counter for how many wins and loses they user has earned 
#TODO add instructions for how to play the game

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
    os.system('cls')
    print("Why did you come here?")
    quit()

#starts keeping score of the game
#keeps track of idk scores
os.system('cls')
print("Awesome lets get started!!!")
time.sleep(2)

end_game_phrase = "no"
continue_playing = "yes"

while True:
    #stores the question and their answers in objects
    Question = question_bank()
    q1 = (question_bank[0], "D"),
    q2 = (question_bank[1], "B"),
    q3 = (question_bank[2], "B"),
    q4 = (question_bank[3], "A"),
    q5 = (question_bank[4], "C"),
    q6 = (question_bank[5], "B"),
    q7 = (question_bank[6], "B"),
    q8 = (question_bank[7], "D"),
    q9 = (question_bank[8], "C"),
    q10 = (question_bank[9], "B"),
    q11 = (question_bank[10], "A"),
    q12 = (question_bank[11], "C"),

    question_bank = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12]


#function to run the game and clear screen for each question for readability
    def quiz(questions):
        os.system('cls')
        score = 0
        x = 1
        for question in questions:
            print(f"Question number: {x}")
            answer = input(random.sample(question.question_bank), 5)
            if answer.isalpha():
                if answer.upper() == question.answer:
                    score += 1
                    x += 1
                    print("Thats the correct answer!!! \n")
                    time.sleep(2)
                    os.system('cls')
                else:
                    print("Darn that is not the correct answer :/ \n\n" + "The correct answer is " + question.answer +"\n")
                    time.sleep(2)
                    os.system('cls')
                    x += 1
            else:
                print("Please enter the correct response the correct response \n")
                x += 1
                continue
            break

#Calls the function
    quiz(question_bank)

    #displays message for score and idk score
    # if Score == 5:
    #     os.system('cls')
    #     print("You got all the questions correct!!!" + "\n")
    #     time.sleep(2)
    #     print("Since you did so well here is one more dad joke" + "\n")
    #     time.sleep(2)
    #     print("What do you call a busy waiter? A server! XD" + "\n") 
    #     time.sleep(2)
    #     print("Thank you for playing!!!")

    # elif Score < 5:
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


