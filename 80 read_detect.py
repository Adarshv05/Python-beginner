with open("80 read_detect.txt", "r") as f:
    if("day" in f.read()):
        print("Detected")
    else:
        print("Not detected")