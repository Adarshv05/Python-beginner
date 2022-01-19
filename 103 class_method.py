class Student:
    a=23
    b=45
    c=54
    @classmethod
    def setAttributes(cls,a,b,c):
        cls.a=a
        cls.b=b
        cls.c=c

stu=Student()
print(Student.a)
print(Student.b)
print(Student.c)

stu.setAttributes(1,2,3)

print(Student.a)
print(Student.b)
print(Student.c)

