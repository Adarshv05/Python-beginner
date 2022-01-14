with open("86 r_w_copyone.txt", "r") as f:
    ar=f.read()

with open("86 r_w_copytwo.txt", "w") as f:
    f.write(ar)
