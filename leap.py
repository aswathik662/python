a=int(input("enter a year"))
if(a%400==0):
    if(a%4==0):
     print("it is a leap year")
    if(a%100==0):
        print("it is not a leap year")
else:
   print("it is not a leap year")
