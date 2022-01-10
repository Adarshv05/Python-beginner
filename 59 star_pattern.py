n=int(input("Enter no. "))

for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print("\n",end="")

# *
# **
# ***