#imports Objects and lists
from question_bank_data import question_prompt
from multiple_choice import Multiple_Choice

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
os.system('clear')
print("Awesome lets get started!!!")
time.sleep(2)

while True:
    #stores the question and their answers in objects
    questions = [
    Multiple_Choice(question_prompt[0], "B"),
    Multiple_Choice(question_prompt[1], "D"),
    Multiple_Choice(question_prompt[2], "C"),
    Multiple_Choice(question_prompt[3], "B"),
    Multiple_Choice(question_prompt[4], "A"),
    ]


#function to run the game and clear screen for each question for readability
    def multiple_choice_quiz(questions):
        # stop_playing = "no"
        # continue_playing = "yes"
        end_of_game = ""      #initializes the end game code 
        while (end_of_game != "yes" and end_of_game != "no"):
            score = 0
            x = 1
            print(f"Question number: {x}")
            for current_question in questions:
                answer = input(current_question.prompt)
                if answer.isalpha():
                    if answer.upper() == current_question.answer:
                        score += 1
                        x += 1
                        print("Current score: " + str(score))
                        print("Thats the correct answer!!! \n")
                        time.sleep(2)
                        
                    else:
                        x += 1
                        print("Current score: " + str(score))
                        print("Darn that is not the correct answer :/ \n\n" + "The correct answer is " + current_question.answer +"\n")
                        time.sleep(2)
                        print(score)
                else:
                    print("Please enter the correct response the correct response \n")
                    continue
                break
            # while (score != 5) or (x == 5):
            #     #displays message for score
            #     if score == 5:
            #             os.system('cls')
            #             print("You got all the questions correct!!!" + "\n")
            #             time.sleep(2)
            #             print("Since you did so well here is one more dad joke" + "\n")
            #             time.sleep(2)
            #             print("What do you call a busy waiter? A server! XD" + "\n") 
            #             time.sleep(2)
            #             print("Thank you for playing!!!")
            #     elif (score < 5):
            #         os.system('cls')
            #         print("Darn you didn't get all the questions correct :/ " + "\n")
            #         time.sleep(2)
            #         print("Go back and try to get all the answers correct! Theres a secret!!!"+ "\n")
            #         time.sleep(2)
            #         print("Thank you for playing!!")
            #     #User should not see this but just in case there is something think of something when testing they will see this message
            #     else:
            #         os.system('cls')
            #         print("How are you seeing this? Go back and play correctly!!" + "\n")
                    
            #         end_of_game = input("do you still want to play?" + "\n")
            #         if end_of_game.lower() == stop_playing:
            #             quit()
            #         elif end_of_game.lower() == continue_playing:
            #             continue
            #         while (end_of_game != "yes" and end_of_game != "no"):
            #             print("Please enter yes or no")
            #             time.sleep(2)
            #             playing = input("Do you want to play? (Yes or no)" + "\n")
            #             if playing.lower() =="yes":
            #                 break
            #             else:
            #                 continue




#Calls the function
    multiple_choice_quiz(questions)

