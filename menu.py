a={}
i=1
while True:
    print("1.register,2.display,3.exti")
    p=int(input("enter the option: "))
    if p==1:
        dict={}
        e=input("enter the name: ")
        d=input("enter the place: ")
        f=int(input("enter your age: "))
        dict["name"]=e
        dict["place"]=d
        dict["age"]=f
        a[i]=dict
        i+=1
    elif p==2:
        flag=0
        # print(a)
        h=input("enter your name:")
        for key in a:
            if a[key]["name"]==h:
                print(a[key])
                flag=1
                break
        if flag==0:
            print("invalid")
           

    elif p==3:
        break
    
         
         