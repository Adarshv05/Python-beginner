class Student:
    def __init__(self,a,name) -> None:
        self.a=a
        self.name=name

    def __add__(self,obj):
        return self.a + obj.a
    
    def __sub__(self,obj):
        return self.a - obj.a
    
    def __mul__(self,obj):
        return self.a * obj.a
    
    def __truediv__(self,obj):
        return self.a / obj.a
    
    def __floordiv__(self,obj):
        return self.a // obj.a

    def __str__(self):
        return self.name

    def __len__(self):
        return self.a

a=Student(50,"John")
b=Student(40,"Kate")

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a,b)
print(len(a))
print(len(b))