with open("83 read_write_replace.txt", "r") as f:
    tx=f.read()

tx=tx.replace("py","Python")

with open("83 read_write_replace.txt", "w") as f:
    f.write(tx)