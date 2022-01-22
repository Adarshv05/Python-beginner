def function():
    try:
        a=int(input("Entre a number : "))
        b=int(input("Entre another number : "))
        print(a / b)
        return a/b

    except Exception as e:
        print(f"Problem :",e)
        return 0

    finally:
        print("This line will always be executed")

print(__name__)
#code run from main file
if __name__ == '__main__':  #same module
    function()
    print("main")

