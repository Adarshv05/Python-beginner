from functools import reduce

def max(x,y):
    if x>y:
        return x
    return y

list=[1,2,3,4,5,4535,657,83,42,35]
a=reduce(max,list)
print(a)
