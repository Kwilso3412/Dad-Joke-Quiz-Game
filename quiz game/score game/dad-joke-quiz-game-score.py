##purpose is to create a dad joke game the user can play.
import sys, os
import time

#puts a delay in between prompts 
print("Welcome to My Quiz!!")
playing = input("Do you want to play? (Yes or no) ")

#TODO print letter by letter for each sentence
#TODO Make a loop for the user to keep playing
#TODO add in a dictionary to hold multiple choice questions with hints
#TODO randomize questions.


    # clear the console when the next thing prompts
    #
#checks to make sure that the user enters in only letters
while True:
    if playing.isalpha():
        break
    else:
        print("Must answer yes or no")
        time.sleep(2)
        playing = input("Do you want to play? (yes or no) ")
        continue

#double checks that the user only enters yes or no
while (playing != "yes" and playing != "no"):
    print("Please enter yes or no")
    time.sleep(2)
    playing = input("Do you want to play? (Yes or no) ")
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

os.system('cls')
print("Awesome lets get started!!!")
time.sleep(2)

os.system('cls')
answer = input("What do sprinters eat before a race? (if not sure say idk) ")
if answer.lower() == "nothing they fast": 
    os.system('cls')
    print("Thats Correct!! Look who has there dad hat on!")
    time.sleep(2)
    Score += 1

elif answer.lower() == "idk":
    os.system('cls')
    print("Nothing They Fast!!!")
    time.sleep(2)
    idk_score += 1

else:
    os.system('cls')
    print("No nothing they fast XD Try to get the next one" )
    time.sleep(2)

os.system('cls')
answer = input("Air use to be free at the gas station, now its a $1.50. You know why? (if not sure say idk) ")
if answer.lower() == "inflation":
    os.system('cls')
    print("Thats Correct!! Your really good at this, do you have some kids on the way?")
    time.sleep(2)
    Score += 1
elif answer.lower() == "idk":
    os.system('cls')
    print("Inflation!!! XD you'll definitely get the next one!!")
    time.sleep(2)
    idk_score += 1
else:
    os.system('cls')
    print("No its because of inflation XD One more you got this!!!")
    time.sleep(2)

os.system('cls')
answer = input("How did the man on the moon cut his hair? (if not sure say idk) ")
if answer.lower() == "he eclipse it":
    os.system('cls')
    print("Thats Correct!! Your definitely a father!!")
    time.sleep(2)
    Score += 1
elif answer.lower() == "idk":
    os.system('cls')
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
    print("You got all the questions correct!!!")
    time.sleep(2)
    os.system('cls')
    print("Since you did so well here is one more dad joke")
    time.sleep(2)
    os.system('cls')
    print("What do you call a busy waiter? A server! XD")
    time.sleep(2)
    os.system('cls')
    print("Thank you for playing!!!")

elif Score < 3 and idk_score <= 3:
    os.system('cls')
    print("Darn you didn't get all the questions correct :/ ")
    time.sleep(2)
    print("Go back and try to get all the answers correct! Theres a secret!!!")
    time.sleep(2)
    os.system('cls')
    print("Thank you for playing!!")

#User should not see this but just in case there is something think of something when testing they will see this message
else:
    os.system('cls')
    print("How are you seeing this? Go back and play correctly!!")
    quit()


