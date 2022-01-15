import os

old=input("File to rename : ")
new=input("New name : ")

with open(old, "r") as f:
    text=f.read()

with open(new, "w") as f:
    f.write(text)

os.remove(old)