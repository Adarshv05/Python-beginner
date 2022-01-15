import random

number=random.randint(1,100)
at=1
guess=int(input("Guess the no. "))

while(True):
  if(guess>number):
     guess=int(input("Guess a no. smaller than this."))
     at=at+1
  elif(guess<number):
     guess=int(input("Guess a no. greater than this."))
     at=at+1
  else:
     print("You Guessed it Right in ",at,"attempts.")
     break;   