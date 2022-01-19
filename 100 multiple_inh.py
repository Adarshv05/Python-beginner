class Parent1:
    a=11

class Parent2:
    b=22

class Child(Parent1, Parent2):
    c=33

cf=Child()
print(cf.a)
print(cf.b)
print(cf.c)