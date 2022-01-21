class vector:
    def __init__(self,i,j,k) -> None:
        self.i=i
        self.j=j
        self.k=k

    def printvector(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")

v1=vector(11,2,4)
v1.printvector()

    
