class Student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def objprint(self):
        print("The name is",self.name)
        print("Marks",self.marks)

    @staticmethod
    def gm():
        print("Cool")

john=Student("John",55)
john.objprint()