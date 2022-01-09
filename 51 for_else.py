a=[1,2,3,4,5,6,7]

for i in a:
    print(i)

    if(i==5):
        break 
    print("Done for",i)
else:
    print("Else executed") #not executed when every el iterated
print("END")

print()

for i in a:
    print(i)

    if(i==5):
        continue
    print("Done for",i)
else:
    print("Else executed")
print("END")

