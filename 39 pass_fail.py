s1=int(input("Sub1 Marks: "))
s2=int(input("Sub2 Marks: "))
s3=int(input("Sub3 Marks: "))

pct=(s1+s2+s3)/3

if(pct>=40):
    if(s1>=33 and s2>=33 and s3>=33):
        print("Pass")
    else:
        print("Fail subject")
else:
    print("Fail overall")            
