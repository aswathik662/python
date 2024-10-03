<<<<<<< HEAD
z=[]
zz=[]
l={"admin":"123"}
def admin():
        b=input("enter username:")
        c=input("enter password:")
        if b in l and l[b]==c:
            print("login successfull")
            while True:
                  print("1.Add Book 2.Update Book 3.Delete Book 4.Display All Books 5.Exit")
                  d=int(input("enter the choice:"))
                  if d==1:
                        add()
                  elif d==2:
                        up()
                  elif d==3:
                        de()
                  elif d==4:
                        dis()
                  elif d==5:
                        break
                  else:
                        print("invalid")
        else:
         print("Invalid login")

def add():
                e=[]
                f=int(input("enter bookid:"))
                if any(f == book[0] for book in z):  
                  print("Book already exists")
                else:
                    g=input("enter title: ")
                    h=input("enter the author: ")
                    i=int(input("enter the quantity:"))
                    e.append(f)
                    e.append(g)
                    e.append(h)
                    e.append(i)
                    z.append(e)
                    print(z)
                    
def up():
                j=int(input("enter the id:"))
                for i in z:
                    if j==i[0]:
                        while True:
                            print("1.title 2.author 3.quantity 4.exit")
                            k=int(input("enter option:"))
                            if k==1:
                                m=input("enter a new title:")
                                i[1]=m
                                print(z)
                            elif k==2:
                                mm=input("enter author:")
                                i[2]=mm
                                print(z)
                            elif k==3:
                                mmm=input("enter the new quantity:")
                                i[3]=mmm
                                print(z)
                            elif k==4:
                                break
                            else:
                              print("Invalid option")
def de():
                n=int(input("enter id: "))
                for i in z:
                        if n==i[0]:
                            z.remove(i)
                            print(z)
                            return  
                print("Book not found")

def dis():
      print(z)

def user():
      while True:
            print("1.registration 2.login 3.exit")
            o=int(input("enter your option:"))
            if o==1:
                  reg()
            elif o==2:
                  log()
            elif o==3:
                  break
            else:
             print("Invalid option.")


def reg():
      
      na=input("enter your name:")
      ag=int(input("enter your age:"))
      adr=input("enter your address:")
      pa=int(input("enter password:"))
      pho =ph()
      us=u()
      detail=[na,ag,adr,pa,pho,us]
      zz.append(detail)
      print(zz)

def ph():
      while True:
        pho=int(input("enter your phone number:"))
        if any(i[4] == pho for i in zz):
                print("already exist")
        else:
                return pho
                
def u():
      while True:
        us=input("enter your username:")
        if any(i[5] == us for i in zz): 
                print("already exist")
        else:
            return us
                
        
def log():
    lo = input("Enter username: ")
    po = int(input("Enter your password: "))
    flag=0
    for i in zz:
        print(i)
        if i[5]==lo and i[3]==po:
            print("Successfully logged in.")
            flag=1
            while True:
                print("1. Display All Books 2. Search Book by Name 3. Exit")
                pr = int(input("Enter your option: "))
                if pr == 1:
                    di()
                elif pr == 2:
                    se()
                elif pr == 3:
                    break
                else:
                    print("Invalid option")
        if flag==0:
            print("Invalid login")

def di():
      print(z)
def se():
      ti=input("enter title:")
      flag=0
      for i in z:
            if ti==i[1]:
                   print("id",i[0])
                   print("title",i[1])
                   print("author",i[2])
                   print("quantity",i[3])
                   flag=1
            if flag==0:
                        print("invalid")
while True:
        print("Main menu")
        print("1.Admin 2.User 3.exit")
        a=int(input("enter choice:"))
        if a==1:
            admin()
        elif a==2:
            user()
        elif a==3:
              break
        else:
            print("invalid choice")

                
        
=======
z=[]
zz=[]
l={"admin":"123"}
def admin():
        b=input("enter username:")
        c=input("enter password:")
        if b in l and l[b]==c:
            print("login successfull")
            while True:
                  print("1.Add Book 2.Update Book 3.Delete Book 4.Display All Books 5.Exit")
                  d=int(input("enter the choice:"))
                  if d==1:
                        add()
                  elif d==2:
                        up()
                  elif d==3:
                        de()
                  elif d==4:
                        dis()
                  elif d==5:
                        break
                  else:
                        print("invalid")
        else:
         print("Invalid login")

def add():
                e=[]
                f=int(input("enter bookid:"))
                if any(f == book[0] for book in z):  
                  print("Book already exists")
                else:
                    g=input("enter title: ")
                    h=input("enter the author: ")
                    i=int(input("enter the quantity:"))
                    e.append(f)
                    e.append(g)
                    e.append(h)
                    e.append(i)
                    z.append(e)
                    print(z)
                    
def up():
                j=int(input("enter the id:"))
                for i in z:
                    if j==i[0]:
                        while True:
                            print("1.title 2.author 3.quantity 4.exit")
                            k=int(input("enter option:"))
                            if k==1:
                                m=input("enter a new title:")
                                i[1]=m
                                print(z)
                            elif k==2:
                                mm=input("enter author:")
                                i[2]=mm
                                print(z)
                            elif k==3:
                                mmm=input("enter the new quantity:")
                                i[3]=mmm
                                print(z)
                            elif k==4:
                                break
                            else:
                              print("Invalid option")
def de():
                n=int(input("enter id: "))
                for i in z:
                        if n==i[0]:
                            z.remove(i)
                            print(z)
                            return  
                print("Book not found")

def dis():
      print(z)

def user():
      while True:
            print("1.registration 2.login 3.exit")
            o=int(input("enter your option:"))
            if o==1:
                  reg()
            elif o==2:
                  log()
            elif o==3:
                  break
            else:
             print("Invalid option.")


def reg():
      
      na=input("enter your name:")
      ag=int(input("enter your age:"))
      adr=input("enter your address:")
      pa=int(input("enter password:"))
      pho =ph()
      us=u()
      detail=[na,ag,adr,pa,pho,us]
      zz.append(detail)
      print(zz)

def ph():
      while True:
        pho=int(input("enter your phone number:"))
        if any(i[4] == pho for i in zz):
                print("already exist")
        else:
                return pho
                
def u():
      while True:
        us=input("enter your username:")
        if any(i[5] == us for i in zz): 
                print("already exist")
        else:
            return us
                
        
def log():
    lo = input("Enter username: ")
    po = int(input("Enter your password: "))
    flag=0
    for i in zz:
        print(i)
        if i[5]==lo and i[3]==po:
            print("Successfully logged in.")
            flag=1
            while True:
                print("1. Display All Books 2. Search Book by Name 3. Exit")
                pr = int(input("Enter your option: "))
                if pr == 1:
                    di()
                elif pr == 2:
                    se()
                elif pr == 3:
                    break
                else:
                    print("Invalid option")
        if flag==0:
            print("Invalid login")

def di():
      print(z)
def se():
      ti=input("enter title:")
      flag=0
      for i in z:
            if ti==i[1]:
                   print("id",i[0])
                   print("title",i[1])
                   print("author",i[2])
                   print("quantity",i[3])
                   flag=1
            if flag==0:
                        print("invalid")
while True:
        print("Main menu")
        print("1.Admin 2.User 3.exit")
        a=int(input("enter choice:"))
        if a==1:
            admin()
        elif a==2:
            user()
        elif a==3:
              break
        else:
            print("invalid choice")

                
        
>>>>>>> dc0e1ae4da810d941227dbee9087de054f1803fe
