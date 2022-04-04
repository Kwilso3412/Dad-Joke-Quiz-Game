##purpose of this file is to create a program that will run the quiz game
from question_bank_data import question_list
from quiz import Quiz_game
from quiz import Question

#import sys, os
import time

#puts a delay in between prompts 
print("Welcome to My Quiz!!")
playing = input("Do you want to play? (Yes or no) ")

#TODO print letter by letter for each sentence
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
        playing = input("Do you want to play? (yes or no)" + "\n")
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
    print("Why did you come here?")
    quit()


#starts keeping score of the game
#keeps track of idk scores
else:
    Score = 0
    idk_score = 0

print("Awesome lets get started!!!")
time.sleep(2)


end_game_phrase = "no"
continue_playing = "yes"

while True:
    #stores the question and their answers in objects
    questions = [
        Question(question_list[0], "D"),
        Question(question_list[1], "B"),
        Question(question_list[2], "B"),
        Question(question_list[3], "A"),
        Question(question_list[4], "C"),
        Question(question_list[5], "B"),
        Question(question_list[6], "B"),
        Question(question_list[7], "D"),
        Question(question_list[8], "C"),
        Question(question_list[9], "B"),
        Question(question_list[10], "A"),
        Question( question_list[11], "C"),
        ]

#this wil loop through the questions and then print out the question
    def run_test(questions):
        for question in questions:
            answer = input(question.question_list)
            if answer == question.answer:
                score += 1

    run_test(questions)
    
#Starts the Quiz game
    #quiz = Quiz_game(question_list)

    

    #while quiz.remaining_questions():
        #quiz.next_question

    #print("You've completed the quiz!!")
    #print(f"Your final score was: {quiz.score}/{quiz.question_number}")

    


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


