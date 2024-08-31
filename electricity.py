a=int(input("enter the number"))
if(a<=100):
    b=a*5
    print(b)
elif(a<=200):
    b=100*5+(a-100)*10
    print(b)
elif(a>200):
    b=100*5+100*10+(a-200)*15
    print(b)
else:
    print("number is invalid")


    

