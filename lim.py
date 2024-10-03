d1={}
while True:
    print("1.Registration\n 2.Login\n 3.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        a=input("Enter a username:")
        if a in d1:
            print("Username already exists")
        else:
            b=int(input("Enter the password"))
            d1[a]=b
            print("Successfully registered")

    elif choice==2:
        username=input("Enter the usename")
        password=int(input("Enter the password"))
        if username in d1 and d1[username]==password:
            print("Successfully logged in")
        else:
            print("Invalid.Please Try again")
    elif choice==3:
        print("Exit")
        break