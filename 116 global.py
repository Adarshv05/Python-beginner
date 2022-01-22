a=5

def function():
    global a
    a=10
    print(a)
    a=20
    print(a)
    
print(a)
function()
print(a)