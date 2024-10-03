class Cal:
    def Add(self,num1,num2):
        return num1+num2
class Sub:
    def Subtract(self,num1,num2):
        return num1-num2
class Mul:
    def multiply(self,num1,num2):
        return num1*num2
class Div(Cal,Sub,Mul):
    def divide(self,num1,num2):
        return num1/num2
    
d=Div()
while True:
            print("\nMenu:")
            print("1. Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
            n=int(input("enter the choice"))
            num1=int(input("enter 1st num"))
            num2=int(input("enter 2nd num"))
            if n==1:
                c=d.Add(num1,num2)
                print(c)

            elif n==2:
                 e=d.Subtract(num1,num2)
                 print(e)
            elif n==3:
                 f=d.multiply(num1,num2)
                 print(f)
            elif n==4:
                 g=d.divide(num1,num2)
                 print(g)
            elif n==5:
                 break
                 

