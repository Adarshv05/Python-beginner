#map
square= lambda x: x*x
l1=[1,2,3,4,5]
a=map(square,l1)
print(list(a))

b= map(lambda x:x*x,[1,2,3,4,5])
print(list(b))

#filter
l2=[1,2,345,56,76,8,3,5,67,78]
greater= lambda x: x>10
c=filter(greater,l2)
print(list(c))

d= filter(lambda x:x>10,[1,2,345,56,76,8,3,4,67,78])
print(list(d))

from functools import reduce
#reduce
l3=[1,2,3,4,5,6,7,8,9]
sum= lambda x,y:x+y
e=reduce(sum,l3)
print(e)

f=reduce(lambda x,y:x+y,[1,2,3,4,5,6,7,8,9])
print(f)