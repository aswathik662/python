l=[]
def user():
    print("1.register 2.login 3.exit")
    e=int(input("enter the option:"))
    if e==1:
        reg()
    elif e==2:
        log()
    elif e==3:
        print("exit")
        
    else:
        print("invalid")
  
def reg():
    ll={} 
    a=input("enter name:")
    b=int(input("enter your age:"))
    c=int(input("enter password:"))
    d=input("enter your username:")
    flag=0
    for i in l:
        if i["username"]==d:
            print("already exist")
            flag=1
        if flag==0:
            return d
    ll["name"]=a
    ll["age"]=b
    ll["password"]=c
    ll["username"]=d
    l.append(ll)
    # print(ll)
          
def log():
    f=input("enter username:")
    g=int(input("enter password:"))
    flag=0
    for i in l:
        if i["username"]==f and i["password"]==g:
            flag=1
            print("login sucessfull")
            
    if flag==0:
        print("try again")
        return log()
while True:
    print("main menu")
    user()