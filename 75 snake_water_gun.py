import random
import pyttsx3
engine=pyttsx3.init()

def game(computer,player):
     if(computer==player):
         print("Draw")
         engine.say("Match Draw")
         engine.runAndWait()
     elif(computer=="s" and player=="g"):
         return True
     elif(computer=="g" and player=="w"):
         return True
     elif(computer=="w" and player=="s"):
         return True
     elif(computer=="g" and player=="s"):
         return False
     elif(computer=="w" and player=="g"):
         return False
     elif(computer=="s" and player=="w"):
         return False
     else:
         print("Enter a Valid Keyword")

choice=("s","w","g")
computer=random.randint(0,2)
computer=choice[computer]
print('''Press s for Snake
Press w for Water
Press g for Gun''')
player=input("Choose Snake, Watre or Gun :")

win=game(computer,player)
print(f"You -> {player} vs Computer -> {computer}")


if win is True:
    print("WIN WIN!")
    engine.say("Winner Winner")
    engine.runAndWait()
elif win is False:
    print("LOSE")
    engine.say("You Lose")
    engine.runAndWait()

