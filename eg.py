z = []  
zz = []  
l = {"admin": "123"}  

def admin():
    b = input("Enter username: ")
    c = input("Enter password: ")
    if b in l and l[b] == c:
        print("Login successful")
        while True:
            print("1. Add Book 2. Update Book 3. Delete Book 4. Display All Books 5. Exit")
            d = int(input("Enter the choice: "))
            if d == 1:
                add()
            elif d == 2:
                up()
            elif d == 3:
                de()
            elif d == 4:
                dis()
            elif d == 5:
                break
            else:
                print("Invalid choice")
    else:
        print("Invalid login credentials")

def add():
    e = []
    f = int(input("Enter book ID: "))
    if any(f == book[0] for book in z):  
        print("Book already exists")
    else:
        g = input("Enter title: ")
        h = input("Enter the author: ")
        i = int(input("Enter the quantity: "))
        e.append(f)
        e.append(g)
        e.append(h)
        e.append(i)
        z.append(e)
        print("Books:", z)

def up():
    j = int(input("Enter the ID: "))
    for i in z:
        if j == i[0]:
            while True:
                print("1. Title 2. Author 3. Quantity 4. Exit")
                k = int(input("Enter option: "))
                if k == 1:
                    m = input("Enter a new title: ")
                    i[1] = m
                    print("Books:", z)
                elif k == 2:
                    mm = input("Enter author: ")
                    i[2] = mm
                    print("Books:", z)
                elif k == 3:
                    mmm = int(input("Enter the new quantity: "))  
                    i[3] = mmm
                    print("Books:", z)
                elif k == 4:
                    break
                else:
                    print("Invalid option")

def de():
    n = int(input("Enter ID: "))  
    for i in z:
        if n == i[0]:
            z.remove(i)
            print("Book deleted")
            print("Books:", z)
            return  
    print("Book not found")

def dis():
    print("Books:", z)

ee = [] 

def user():
    while True:
        print("1. Registration 2. Login 3.exist")
        o=int(input("Enter your option: "))
        if o==1:
            reg()
        elif o==2:
            log()
        elif o==3:
            break
        else:
            print("Invalid option.")

def reg():
    na = input("Enter your name: ")
    ag = int(input("Enter your age: "))
    adr = input("Enter your address: ")
    pa = input("Enter your password: ")  
    pho = ph()
    us = u()
    user_details = [na, ag, adr, pa, pho, us]  
    zz.append(user_details)
    print("Users:", zz)

def ph():
    while True:
        pho = input("Enter your phone number: ")  
        if any(i[4] == pho for i in zz):
            print("Phone number already exists")
        else:
            return pho

def u():
    while True:
        us = input("Enter your username: ")
        if any(i[5] == us for i in zz):
            print("Username already exists")
        else:
            return us

def log():
    lo = input("Enter username: ")
    po = input("Enter your password: ")
    for i in zz:
        if i[5] == lo and i[3] == po:
            print("Successfully logged in.")
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
            return
    print("Invalid login credentials")

def di():
    print("Books:", z)

def se():
    ti = input("Enter title: ")
    found = False
    for i in z:
        if ti == i[1]:
            print("ID:", i[0])
            print("Title:", i[1])
            print("Author:", i[2])
            print("Quantity:", i[3])
            found = True
    if not found:
        print("Book not found")

while True:
    print("Main menu")
    print("1. Admin 2. User")
    a = int(input("Enter choice: "))
    if a == 1:
        admin()
    elif a == 2:
        user()
    else:
        print("Invalid choice")