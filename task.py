a=[]
while True:
    print("MAIN MENU\n")
    print("1.Add Task:2.View All Tasks:3.Update Task:4. Mark Task as Completed:5.Delete Task:6.Search Task by Name:7.exit:")
    b=int(input("enter the option: "))
    if b==1:
        c=[]
        d=input("enter the name: ")
        if d in a:
            print("Username already exists")
        else:
            e=input("enter the description: ")
            f=int(input("enter due date: "))
            g=(input("enter priority level: "))
            c.append(e)
            c.append(d)
            c.append(f)
            c.append(g)
            a.append(c)
    elif b==2:
        print(a)
    elif b==3:
        flag=0
        z=input("enter the task name:")
        for i in a:
            if z in i[0]:
                while True:
                    print("1.name 2.description 3.date 4.priority 5.exit")
                    q=int(input("enter choice:"))
                    if q==1:
                        t=input("enter a new name:")
                        i[0]=t
                        
                    elif q==2:
                         tt=input("enter description: ")
                         i[1]=tt
                    elif q==3:
                         ttt=int(input("enter date: "))
                         i[2]=ttt
                    elif q==5:
                        break
                    elif q==4:
                         tttt=input("enter priority:")
                         i[3]=tttt
                         flag=1
        if flag==0:
             print("invalid")
        
    elif b==4:
         flag=0
         m=input("enter name: ")
         for i in a:
            if m in i[0]:
                n=input("task completed or not completed: ")
                i.append(n)
                flag=1
         if flag==0:
            print("invalid")
    elif b==5:
        flag=0
        o=input("enter name: ")
        for i in a:
            if o in i[0]:
                a.remove(i)
                flag=1
        if flag==0:
             print("invalid")
    elif b==6:
         flag=0
         pp=input("enter name: ")
         for i in a:
                if pp in i[0]:
                     print("name",i[0])
                     print("description",i[1])
                     print("date",i[2])
                     print("priority",i[3])
                     flag=1
         if flag==0:
          print("invalid")
    elif b==7:
        break
    else:
        print("number is invalid")
            
