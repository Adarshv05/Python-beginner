def greatest(n1,n2,n3):
    if(n1>n2):
        gr=n1
    else:
        gr=n2
    if(n3>gr):
        gr=n3
    
    return gr

a=greatest(43,345,235)
print(a)