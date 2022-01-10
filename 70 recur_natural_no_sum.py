def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

# a=sum(6)
# print(a)

a=int(input("Enter n "))
print(sum(a))