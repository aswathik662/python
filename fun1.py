def sum(b,c):
    print(b+c)
def sub(b,c):
    print(b-c)
def mul(b,c):
    print(b*c)
def div(b,c):
    print(b/c)

while True:
    print("MAIN MENU")
    print("1.addition 2.subtraction 3.multiplication 4.division 5.exit")
    a=int(input("enter the option:"))
    
    if a==1:
        b=int(input("enter 1st number: "))
        c=int(input("enter 2nd number:"))
        sum(b,c)
    elif a==2:
       b=int(input("enter 1st number: "))
       c=int(input("enter 2nd number:"))
       sub(b,c)
    elif a==3:
        b=int(input("enter 1st number: "))
        c=int(input("enter 2nd number:"))
        mul(b,c)
    elif a==4:
        b=int(input("enter 1st number: "))
        c=int(input("enter 2nd number:"))
        div(b,c)
    elif a==5:
        break
    else:
        print("invalid option")
