l=int(input("enter the number"))
if l<=1:
    print("it is not prime")
else:
    for i in range(2,l):
        if(l%i==0):
            print("it is not prime")
        else:
         print("is a prime")



