score=int(input("Enter Your Score "))

if(score>90 and score<=100):
    print("A+")

elif(score>80 and score<=90):
    print("A")

elif(score>70 and score<=80):
    print("B")

elif(score>60 and score<=70):
    print("C")

elif(score>50 and score<=60):
    print("D")

elif(score<50 and score>=0):
    print("F")

else:
    print("Enter a Valid Number")
