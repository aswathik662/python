gus=[]
rev=0
guest=[]
rp=[]
dd=[]
ro=1
ad={"admin":"123"}
rece={"recc":"1234"}


def admin():
    b=input("enter username:")
    c=(input("enter password:"))
    if b in ad and ad[b]==c:
        print("successfully login")
        while True:
            print("1.Add Room \n2.Update Room Details\n 3.Remove Room \n  4.View All Reservations\n 5.Generate Reports\n 6.display\n 7.Exit")
            d=int(input("enter your choice:"))
            if d==1:
                add()
            elif d==2:
                up()
            elif d==3:
                de()
            elif d==4:
                vi()
            elif d==5:
                ge()
            elif d==6:
                dis()

            elif d==7:
                break
    else:
            print("invalid password and name")

def dis():
    for i in dd:
        print("num",i[0])
        print("room type",i[1]) 
        print("price",i[2])
        print("availablity ststus",i[3]) 
        
def add():
    global ro
    ddd=[]
    e=ro
    f=input("room type:")
    g=int(input("enter price per night: "))
    h="available"
    ddd.append(e)
    ddd.append(f)
    ddd.append(g)
    ddd.append(h)
    dd.append(ddd)
    ro+=1
def up():
    ii = int(input("Enter room number to update: "))
    flag=0
    for i in dd:
        if i[0]==ii:
            flag=1
            while True:
                print("1. Update price\n 2. Update availability status\n 3. Exit")
                j=int(input("Enter option: "))
                if j==1:
                    k=int(input("Enter the new price: "))
                    i[2]=k
                
                elif j==2:
                    kk=input("New status of the room: ")
                    i[3]=kk
                
                elif j == 3:
                    break  
                else:
                    print("Invalid option")
    if flag==0:
            print("Room number does not match")
def de():
    l=int(input("Enter room number to remove: "))
    for i in dd:
        if i[0]==l:
            dd.remove(i)
            return
    print("Room number does not exist")

def vi():
    rs="reserved"
    if len(rp)==0:
        print("no reservation")
    else:
        for i in rp:
            if i[4]==rs:
                print("guest id",i[0])
                print("room no",i[1])
                print("check in",i[2])
                print("check out",i[3])
    
   
def ge():
    count=0
    o=0
    for i in dd:
        if i[3]=="available":
            count+=1
        elif i[3]=="occupied":
            o+=1
            
    print("ocuppied rate",o)
    print("available room",count)
    m=int(input("enter revenue generated:"))
    dd.append(m)
    
   

def rec():
    rr = input("Enter username: ")
    rrr = input("Enter password: ")  
    if rr in rece and rece[rr] == rrr:
        print("succcessfuly login")
        while True:
            print("1.Check-In Guest 2.Check-Out Guest 3.Make Reservation 4.Cancel Reservation 5.View Available Rooms 6.View Guest Details 7.Exit")
            ra=int(input("enter choice:"))
            if ra==1:
                raa()
            elif ra==2:
                rc()
            elif ra==3:
                rd()
            elif ra==4:
                re()
            elif ra==5:
                rf()
            elif ra==6:
                rg()
            elif ra==7:
                break
            else:
                print("invalid option")
    else:
        print("invalid password")


def raa():
    
    en=input("enter guest id:")
    flag=0
    for i in gus:
        if en==i[0] :
            flag=1
            print("guest id",i[0])
            print("name",i[1])
            print("adress",i[2])
            print("number",i[3])
            # print("room number",i[6])
    ml=int(input("enter room number:"))
    for i in dd:
        if ml==i[0]:
            i[3]="occupied"
    if flag==0:
            print("invalid")
   

def rc():
    # coi=int(input("enter guest id:"))
    con=int(input("enter room no:"))
    for i in dd:
        if  i[0]==con:
           i[3]="available"
           
               
                # dd.append(av)
    else:
        print("invalid")
def rd():
    rf=[]
    gd=input("guest id:")
    gm=int(input("room no:"))
    cig=int(input("check in date:"))
    cog=int(input("check out date:"))
    cav="reserved"
    rf.append(gd)
    rf.append(gm)
    rf.append(cig)
    rf.append(cog)
    rf.append(cav)
    rp.append(rf)
    for i in dd:
        if i[0]==gm:
           
            i[3]="reserved"
            

def re():
    guid=int(input("enter guest id:"))
    for i in rp:
        if guid == i[0]:
            rp.remove(i)
    else:
            print("invalid")
    
def rf():
    flag=0
    for i in dd:
        if "available"==i[3]:
            flag=1
            print("room type",i[1])
            print("price",i[2])
            print("status",i[3])
    if flag==0:
        print("no rooms available")
           
def rg():
    for i in gus:
        print("name",i[1])
        print("adress",i[2])
        print("phone",i[3])
        print("room no",i[0])

def gu():
    while True:
        print("1. Registration 2. Login 3.exit")
        gr = int(input("Enter option: "))
        if gr == 1:
            ggd = input("Enter guest ID: ")
            
            if any(guest[0] == ggd for guest in gus):
                print("ID already exists")
            else:
                name = input("Enter name: ")
                adr = input("Enter address: ")
                num = input("Enter phone number: ")
                us = input("Username: ")
                pas = input("Enter password: ")
                # rn=int(input("room number:"))
                guest = [ggd, name, adr, num, us, pas]
                gus.append(guest)
                
        elif gr == 2:
            grr = input("Enter username: ")
            grrr = input("Enter password: ")
            for guest in gus:
                if guest[4] == grr and guest[5] == grrr: 
                    print("Login successful")
                    while True:
                        print("1.View Available Rooms\n 2.Make a Reservation\n 3.View Reservation Status\n 4.Update Personal Information\n 5.Cancel Reservation\n 6.Exit")
                        pp = int(input("Enter your choice: "))
                        if pp == 1:
                            ga()
                        elif pp == 2:
                            rd()
                        elif pp == 3:
                            gd(guest)
                        elif pp == 4:
                            gc()  
                        elif pp == 5:
                            gee()
                        elif pp == 6:
                            break
                        else:
                            print("invalid option")

                else:
                    print("invalid password") 
        elif gr==3:
            break   

def ga():
    au="available"
    flag=0
    for i in dd:
        if au==i[3]:
            flag=1
            print("room type",i[1])
            print("room price",i[2])
            print("room no",i[0])
            print("availablity status",i[3])
    if flag==0:
        print("no room available")

# def gb():
            
    # bb = int(input("Enter room number: "))
    # for i in dd:
    #     if bb == i[0]:
    #         ci = input("Check-in date: ")
    #         co = input("Check-out date: ")
    #         guest.append(ci)
    #         guest.append(co)
    #         gus.append(guest)

            
    #         return
    # print("Invalid room number")
def gd(guest):
    for i in rp:
       if guest[0]==i[0]:
            print("reservaton status",i[4])
            print("check in",i[2])
            print("check out",i[3])

def gc():
    user= input("Enter guest ID: ")
    for guest in gus:
        if user== guest[0]:  
            ud = input("Enter new phone number: ")
            ua = input("Enter new address: ")
            guest[3] = ud  
            guest[2] = ua  
            
            return
    print("Invalid guest ID")


def gee():
   uss = int(input("Enter room no: "))
   for i in dd:
        if uss == i[0]:  
            i[3]="available"
            
            
            
while True:
    print("MAIN MENU")
    print("1.ADMIN 2.RECEPTIONIST 3.GUEST 4.exit")
    a=int(input("enter your choice:"))
    if a==1:
        admin()
    elif a==2:
        rec()
    elif a==3:
        gu()
    elif a==4:
        break
    else:
        print("invalid choice")
