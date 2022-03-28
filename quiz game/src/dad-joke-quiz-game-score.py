##purpose is to create a dad joke game the user can play.
import sys, os
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
        os.system('cls')
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
    os.system('cls')
    answer = input("What do sprinters eat before a race? (if not sure say idk) " + "\n")
    if answer.lower() == "nothing they fast": 
        os.system('cls')
        print("Thats Correct!! Look who has there dad hat on!")
        time.sleep(2)
        Score += 1

    elif answer.lower() == "idk":
        print("Nothing They Fast!!!")
        time.sleep(2)
        idk_score += 1

    else:
        print("No nothing they fast XD Try to get the next one" )
        time.sleep(2)

    os.system('cls')
    answer = input("Air use to be free at the gas station, now its a $1.50. You know why? (if not sure say idk) " + "\n")
    if answer.lower() == "inflation":
        print("Thats Correct!! Your really good at this, do you have some kids on the way?")
        time.sleep(2)
        Score += 1
    elif answer.lower() == "idk":
        print("Inflation!!! XD you'll definitely get the next one!!")
        time.sleep(2)
        idk_score += 1
    else:
        print("No its because of inflation XD One more you got this!!!")
        time.sleep(2) 

    os.system('cls')
    answer = input("How did the man on the moon cut his hair? (if not sure say idk)"+ "\n")
    if answer.lower() == "he eclipse it":
        print("Thats Correct!! Your definitely a father!!")
        time.sleep(2)
        Score += 1
    elif answer.lower() == "idk":
        print("He Eclipse it!!! XD Try putting on some cargo shorts to help bring out your inner dad!!")
        time.sleep(2)
        idk_score += 1
    else:
        os.system('cls')
        print("Haha no he eclipse it")
        time.sleep(2)

    #displays message for score and idk score
    if Score == 3:
        os.system('cls')
        print("You got all the questions correct!!!" + "\n")
        time.sleep(2)
        print("Since you did so well here is one more dad joke" + "\n")
        time.sleep(2)
        print("What do you call a busy waiter? A server! XD" + "\n") 
        time.sleep(2)
        print("Thank you for playing!!!")

    elif Score < 3 and idk_score <= 3:
        os.system('cls')
        print("Darn you didn't get all the questions correct :/ " + "\n")
        time.sleep(2)
        print("Go back and try to get all the answers correct! Theres a secret!!!"+ "\n")
        time.sleep(2)
        print("Thank you for playing!!")

    #User should not see this but just in case there is something think of something when testing they will see this message
    else:
        os.system('cls')
        print("How are you seeing this? Go back and play correctly!!" + "\n")


    end_of_game = input("do you still want to play?" + "\n")

    if end_of_game.lower() == end_game_phrase:
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


