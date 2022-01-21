class vector:
    def __init__(self,l1):
        self.dimenstion=len(l1)
        self.data=l1

    def __add__(self,obj):
        list=[]
        for i in range(len(obj.data)):
            list.append(obj.data[i] + self.data[i])
        return vector(list)
    
    def __mul__(self,obj):
        dt=0
        for i in range(len(obj.data)):
            dt= (obj.data[i] * self.data[i])
        return dt

    def __len__(self):
        return len(self.data)

v1=vector([2, 5, 7])
v2=vector([4, 8, 9])
v3=v1+v2
v4=v1*v2
print(v3.data)
print(v4)
print(len(v1))