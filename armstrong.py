num=int(input("enter a number"))
while(num!=0):
       rem=num%10
       sum=sum+(rem*rem*rem)
       n=n/10
       if(num==sum):
   
                print("it is a armstrong number")
else:
     print("it is not a armstrong number")
  
   
