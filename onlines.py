bod = []
rr = 1
ir = 1
us = []
l = []
adc = {"a": "1"}  # Changed key to match admin login

def admin():
    b = input("Enter username: ")
    c = input("Enter password: ")
    if b in adc and adc[b] == c:
        print("Login successful")
        while True:
            print("1. Add Product\n2. Update Product\n3. Remove Product\n4. View All Products\n5. View Orders\n6. Exit")
            d = int(input("Enter the option: "))
            if d == 1:
                add()
            elif d == 2:
                up()
            elif d == 3:
                re()
            elif d == 4:
                via()
            elif d == 5:
                vio()
            elif d == 6:
                break
    else:
        print("Invalid username or password")

def add():
    global rr
    ll = []
    e = rr
    ee = input("Enter a product: ")
    f = input("Enter description: ")
    g = int(input("Enter price: "))
    ll.append(e)
    ll.append(ee)
    ll.append(f)
    ll.append(g)
    l.append(ll)
    rr += 1

def up():
    h = int(input("Enter product ID: "))
    for i in l:
        if i[0] == h:
            while True:
                print("1. New product\n2. New description\n3. New price\n4. Exit")
                pp = int(input("Enter the choice: "))
                if pp == 1:
                    ii = input("Enter the new product: ")
                    i[1] = ii
                elif pp == 2:
                    j = input("New description: ")
                    i[2] = j
                elif pp == 3:
                    jj = int(input("New price: "))
                    i[3] = jj
                elif pp == 4:
                    break
                else:
                    print("Invalid option")
            return  
    print("ID is invalid.")

def re():
    k = int(input("Enter ID: "))
    for i in l:
        if i[0] == k:
            l.remove(i)
            print("Product removed successfully.")
            return
    print("ID does not exist")

def via():
    for i in l:
        print("ID:", i[0])
        print("Product:", i[1])
        print("Description:", i[2])
        print("Price:", i[3])

def vio():
    for i in bod:
        print("Product:", i[0])
        print("Quantity:", i[1])
        print("Name:", i[2])
        print("Address:", i[3])
        print("ID:", i[4])
        print("Order Status:", i[5])

def user():
    global ir
    while True:
        print("1. REGISTER\n2. LOGIN\n3. EXIT")
        uu = int(input("Enter your choice: "))
        if uu == 1:
            id = ir
            na = input("Input username: ")
            em = input("Enter email: ")
            adr = input("Enter address: ")
            pas = input("Enter password: ")
            us.append([id, na, em, adr, pas])
            ir += 1
        elif uu == 2:
            ee = input("Enter username: ")
            eee = input("Enter password: ")
            for i in us:
                if i[1] == ee and i[4] == eee:
                    print("Login successful")
                    while True:
                        print("1. View All Products\n2. Place Order\n3. View Order History\n4. Exit")
                        lo = int(input("Enter choice: "))
                        if lo == 1:
                            via()
                        elif lo == 2:
                            po()
                        elif lo == 3:
                            voh()
                        elif lo == 4:
                            print("Exiting from user")
                            break
                else:
                    print("Invalid username or password")
        elif uu == 3:
            break

def po():
    bb = []
    pr = input("Enter the product: ")
    for i in l:
        if i[1] == pr:
            prr = int(input("Enter the quantity: "))
            np = input("Enter name: ")
            npp = input("Enter address: ")
            nppp = int(input("Enter ID: "))
            bb.append(pr)
            bb.append(prr)
            bb.append(np)
            bb.append(npp)
            bb.append(nppp)
            os = "processing"
            bb.append(os)
            bod.append(bb)
            print("Order placed successfully")
            return
    print("Product not found")

def voh():
    nn = input("Enter the name: ")
    flag = 0
    for i in bod:
        if i[2] == nn:
            flag = 1
            print("Product:", i[0])
            print("Quantity:", i[1])
            print("Name:", i[2])
            print("Address:", i[3])
            print("ID:", i[4])
            print("Order Status:", i[5])
    if flag == 0:
        print("No orders found")

while True:
    print("MAIN MENU")
    print("1. ADMIN\n2. USER\n3. EXIT")
    a = int(input("Enter option: "))
    if a == 1:
        admin()
    elif a == 2:
        user()
    elif a == 3:
        break
    else:
        print("Invalid option")
