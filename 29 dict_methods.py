oxford={
"car":"a road vehicle with four wheels",
"bike":"a bicycle or a motorbike",
"scooty":"a motorized scooter",
"boat":"a small vessel for travelling over water",
"list":[1,5,8,13]    
}

#print(oxford.items())
for a,b in oxford.items():
    print(a,b)

#print(oxford.keys())
for key in oxford.keys():
    print(key)

oxford.update({"aeroplane":"a powered flying vehicle"})
print(oxford.items())

# print(oxford[jet]) error
print(oxford.get("jet"))
#this will print none insted of throwing error