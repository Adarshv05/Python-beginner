num=int(input("Enter a number :"))

mp=[i*num for i in range(1,11)] #because range is (a,b-1)
print(mp)

with open("123 mpt.txt","w") as f:
    f.write(str(mp))