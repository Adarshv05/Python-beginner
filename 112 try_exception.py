try:
    print("Yooo Boiss")
    a=int(input("Entre a number : "))
    b=int(input("Entre another number : "))
    print(a / b)

except ValueError:
    print("Value Error Occurred")

except ZeroDivisionError:
    print("Zero Division Error Occurred")

except Exception as e:
    print(f"Problem :",e)

print("Remaining Program Will be executed")

