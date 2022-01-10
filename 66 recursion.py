def factorial(n):
    #Base condition to stop infinite loop
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

a=factorial(5)
print(a)
