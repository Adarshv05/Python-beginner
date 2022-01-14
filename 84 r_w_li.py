with open("84 r_w_li.txt", "r") as f:
    tx=f.read()

list=["yo","text"]
for item in list:
    tx=tx.replace(item,"*****")

with open("84 r_w_li.txt", "w") as f:
    f.write(tx)