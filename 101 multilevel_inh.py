class Parent:
    a=11

class Child1(Parent):
    b=22

class Child2(Child1):
    c=33

cf=Child2()
print(cf.a)
print(cf.b)
print(cf.c)
   