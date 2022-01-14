with open("85 r_w_chk.txt","r") as f:
    tx=f.read()
    
if 'Python' in tx:
    print("True")
else:
    print("False")