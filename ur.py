s={}

while True:
    print("1.register 2.login 3.exit")
    n=int(input("enter your choice: "))
    if n==1:
     a=input("enter your username: ")
     if a in s:
       print("already exist")
     b=int(input("enter your password: "))
     s["username"]=a
     s["password"]=b
    else:
      p=input("enter username:")
      p==a
    elif n==2:
    flag=0
    c=input("enter username: ")
    d=int(input("enter password: "))
    for i in s:
          if s[i]["username"]==c and s[i]["password"]==d:
             print("successfully logged in",s[i])
             flag=1
             break
    if flag==0:
             print("try again")
    elif n==3:
       break


     
