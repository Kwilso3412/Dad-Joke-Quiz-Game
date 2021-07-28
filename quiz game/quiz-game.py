import time

print("Welcome to My Quiz!!")

playing = input("Do you want to play? (Yes or no) ")

if playing.lower() !="yes":
    quit

#starts keeping score of the game

print("Awesome lets get started!!!")
Score = 0

answer = input("What do sprinters eat before a race? (if not sure say idk) ")
if answer.lower() == "nothing they fast": 
    pause
    print("Thats Correct!! look who has there dad hat on")
    Score += 1

elif answer.lower() == "idk":
    
    print("Nothing They Fast!!!")


answer = input("Air use to be free at the gas station, now its a $1.50. You know why? (if not sure say idk) ")
if answer.lower() == "inflation":
    
    print("Thats Correct!! Your really good at this do you have some kids on the way?")
    Score += 1

elif answer.lower() == "idk":
    
    print("Inflation!!! XD come on you will definitely get the next one")


answer = input("How did the man on the moon cut his hair? (if not sure say idk) ")
if answer.lower() == "he eclipse it":
    
    print("Thats Correct!! Your definitely a father!!")
    Score += 1

elif answer.lower() == "idk":
    print("He Eclipse it!!! XD try putting on some cargo shorts to help bring out your inner dad!!")

#converts teh int score into string score
print("You got " + str(Score) + " Questions correct!")
print("Your grade: " + str((Score/3) * 100) + "%.")
