class Parent:
    a=11
    def __init__(self):
        print("Parent")

class Child1(Parent):
    b=22
    def __init__(self):
        print("Child 1")
        super().__init__()

class Child2(Child1):
    c=33
    def __init__(self):
        print("Child 2")
        super().__init__()

cf=Child2()
print(cf.a)
print(cf.b)
print(cf.c)
   