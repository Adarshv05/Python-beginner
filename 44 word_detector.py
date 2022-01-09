from typing import Text


text =input("Enter text :")
word=input("Enter det word: ")
if word.lower() in text.lower():
    print("Detected")
else:
    print("Not Detected")
     