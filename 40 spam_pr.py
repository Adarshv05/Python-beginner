spamkey=["buy it now","follow us","click this"]

email=input("Enter Mail :").lower()

if("buy it now" in email):
    print("Spam")
if("follow us" in email):
    print("Spam")
if("click this" in email):
    print("Spam")
else:
    print("Clean")
