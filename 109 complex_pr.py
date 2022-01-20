class Complex:
    def __init__(self,a, b):
        self.a=a #real
        self.b=b #imaginary

    def __add__(self, obj):
        return Complex(self.a + obj.a, self.b + obj.b)
    
    def __mul__(self,obj):
        return Complex(self.a*self.b - obj.a*obj.b, self.a*obj.b + obj.a*self.b)

c1=Complex(3,2)
c2=Complex(1,7)

c3=c1+c2
print(c3.a,c3.b)

c4=c1*c2
print(c4.a,c4.b)

