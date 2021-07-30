import time

print("Welcome to My Quiz!!")
playing = input("Do you want to play? (Yes or no) ")
#checks to make sure that the user enters in only letters
while True:
    if playing.isalpha():
        break
    else:
        print("Must answer yes or no")
        playing = input("Do you want to play? (yes or no) ")
        continue

#double checks that the user only enters yes or no
while (playing != "yes" and playing != "no"):
    print("please enter yes or no")
    playing = input("Do you want to play? (Yes or no) ")
    if playing.lower() =="yes":
        print("Awesome lets get started!!!")
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

answer = input("What do sprinters eat before a race? (if not sure say idk) ")
if answer.lower() == "nothing they fast": 
    print("Thats Correct!! look who has there dad hat on")
    Score += 1
elif answer.lower() == "idk":
    print("Nothing They Fast!!!")
    idk_score += 1
else:
    print("no nothing they fast XD come one lets see if you can get the next one" )

answer = input("Air use to be free at the gas station, now its a $1.50. You know why? (if not sure say idk) ")
if answer.lower() == "inflation":
    
    print("Thats Correct!! Your really good at this do you have some kids on the way?")
    Score += 1
elif answer.lower() == "idk":
    print("Inflation!!! XD come on you will definitely get the next one")
    idk_score += 1
else:
    print("no its because of inflation XD one more you got this")


answer = input("How did the man on the moon cut his hair? (if not sure say idk) ")
if answer.lower() == "he eclipse it":
    
    print("Thats Correct!! Your definitely a father!!")
    Score += 1
elif answer.lower() == "idk":
    print("He Eclipse it!!! XD try putting on some cargo shorts to help bring out your inner dad!!")
    idk_score += 1
else:
    print("Haha no he eclipse it")

#converts the int score into string score and tells the user their score
str(Score)

#displays message for score 
if Score == 3:
    print("You got all the questions correct!!!")
    print("Since you did so well here is one more dad joke")
    print("What do you call a busy waiter? A server! XD")
else:
    print("Darn you didn't get all the questions go back and try again you might get a secret message")

#displays message for idk score
if idk_score == 3:
    print("whoops it looks like you answered idk to all go try again to get a secret message")
elif idk_score >= 1:
    print("looks like you you answered idk to some of the questions go back you might get a secret message if you get them all correct!")
else:
    print("Thank you for playing!")

