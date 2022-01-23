list1=[1,2,3,4,5,6,7,8,9]

for i,item in enumerate(list1):
    if(i==2 or i==4 or i==6):
        print(item)

list2=[1,2,3,4,5,6,7,8,9]

for index,item in enumerate(list2):
    if(index+1==3 or index+1==5 or index+1==7):
        print(item)
