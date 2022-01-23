try:
    with open("1.txt", "r") as f:
        f.read()
        
    with open("2.txt", "r") as f:
        f.read()

except Exception as e:
    print(f"File not present -> {e}")

print("Boiss")