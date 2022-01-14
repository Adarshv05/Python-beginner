with open("87 r_w_compare1.txt", "r") as f:
    c1=f.read()

with open("87 r_w_compare2.txt", "r") as f:
    c2=f.read()

if c1==c2:
    print("Match")
else:
    print("Not")
