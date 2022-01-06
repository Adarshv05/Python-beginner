hind={
    "kapda":"cloth",
    "chai":"tea",
    "lakdi":"wood"
}
key=input("Enter the key\n")
if(hind.get(key)==None):
    print("Not found")
else:
    print(key,":",hind.get(key))