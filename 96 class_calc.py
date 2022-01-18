import math
class Calculator:
    def __init__(self,number):
         self.number=number
    
    def square(self):
         return self.number * self.number
    
    def squareRoot(self):
         return math.sqrt(self.number)
    
    def cube(self):
         return self.number * self.number * self.number
    
    @staticmethod 
    def gm():
        print("Cool")

three=Calculator(3)
three.gm()
print(three.number)
print(three.square())
print(three.squareRoot())
print(three.cube())

    