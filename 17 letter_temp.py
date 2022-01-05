name=input("Enter Name ")
date=input("Enter Date ")

temp='''
Dear <name>,
You are selected
<date>'''

print(temp.replace("<name>",name).replace('<date>',date))

