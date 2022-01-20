class vector2d:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def printvector(self):
        print(f"{self.i}i + {self.j}j")

class vector3d(vector2d):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def printvector(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")

v2=vector2d(33,55)
v3=vector3d(45,67,98)

v2.printvector()
v3.printvector()

