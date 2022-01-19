class Student:
    a=23
    b=45
    c=54
    @classmethod
    def setAttributes(cls,a,b,c):
        cls.a=a
        cls.b=b
        cls.c=c

    @property
    def length(self):
        return self.a

    @length.setter
    def length(self,value): #function with property decorator
        self.a=value

stu=Student()
stu.setAttributes(1,2,3)
print(stu.length)
stu.length=66
print(stu.length)
