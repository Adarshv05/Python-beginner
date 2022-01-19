class Student:
    a=77

class Programmer(Student): # child class
    b=80

pr=Programmer()
print(pr.a)
print(pr.b) 

st=Student()
print(st.a)
# print(st.b) 'Student' object has no attribute 'b' 
