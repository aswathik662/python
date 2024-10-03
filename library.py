class Adb:
    l = []

    def __init__(self, bi, ti, aut, qua):
        self.bi = bi
        self.ti = ti
        self.aut = aut
        self.qua = qua

    def add(self):
        Adb.l.append(self)

    def update(self, ti, aut, qua):
        self.ti = ti
        self.aut = aut
        self.qua = qua

    @classmethod
    def dele(cls, bi):
        for book in cls.l:
            if book.bi == bi:
                cls.l.remove(book)
                return True
        return False

    @classmethod
    def display(cls):
        if cls.l:
            return [str(book) for book in cls.l]
        return []

    @classmethod
    def search(cls, ti):
        results = []
        for book in cls.l:
            if ti.lower() in book.ti.lower():
                results.append(book)
        return results

    def __str__(self):
        return f"id: {self.bi}, title: {self.ti}, author: {self.aut}, quantity: {self.qua}"


class Admin:
    b = {"a": "1"}  # Example admin credentials

    def login(self):
        c = input("Enter username: ")
        d = input("Enter password: ")
        if c in self.b and self.b[c] == d:
            print("Successfully logged in")
            self.manage()
        else:
            print("Invalid credentials")

    def manage(self):
        while True:
            print("1. Add Book\n2. Update Book\n3. Delete Book\n4. Display All Books\n5. Exit")
            e = int(input("Enter your choice: "))
            if e == 1:
                bi = int(input("Enter book ID: "))
                ti = input("Enter book title: ")
                aut = input("Enter book author: ")
                qua = int(input("Enter book quantity: "))
                book = Adb(bi, ti, aut, qua)
                book.add()
                print("Book added successfully.")
            elif e == 2:
                bi = int(input("Enter book ID: "))
                for book in Adb.l:
                    if book.bi == bi:
                        ti = input("Enter new book title: ")
                        aut = input("Enter new book author: ")
                        qua = int(input("Enter new book quantity: "))
                        book.update(ti, aut, qua)
                        print("Updated successfully")
                        break
                else:
                    print("Book not found")
            elif e == 3:
                bi = int(input("Enter book ID: "))
                if Adb.dele(bi):
                    print("Book deleted")
                else:
                    print("Book not found")
            elif e == 4:
                books = Adb.display()
                if books:
                    for book in books:
                        print(book)
                else:
                    print("No books available.")
            elif e == 5:
                print("Exiting")
                break
            else:
                print("Invalid choice")


class Up:
    def __init__(self, name, age, addr, pho, uname, pas):
        self.name = name
        self.age = age
        self.addr = addr
        self.pho = pho
        self.uname = uname
        self.pas = pas


class User:
    users = {}

    def regi(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        addr = input("Enter your address: ")
        pho = input("Enter your phone number: ")
        uname = input("Enter a username: ")
        pas = input("Enter a password: ")
        if pho in [user.pho for user in User.users.values()] or uname in User.users:
            print("Phone number or username already exists. Registration failed.")
            return
        User.users[uname] = Up(name, age, addr, pho, uname, pas)
        print("Registration successful.")

    def login(self):
        uu = input("Enter username: ")
        upp = input("Enter password: ")
        if uu in User.users and User.users[uu].pas == upp:
            print("Login successful.")
            self.um()
        else:
            print("Invalid credentials")

    def um(self):
        while True:
            print("1. Display All Books\n2. Search Book by Name\n3. Exit")
            cc = int(input("Enter your choice: "))
            if cc == 1:
                books = Adb.display()
                if books:
                    for book in books:
                        print(book)
                else:
                    print("No books available.")
            elif cc == 2:
                ti = input("Enter the book title to search: ")
                results = Adb.search(ti)
                if results:
                    for book in results:
                        print(book)
                else:
                    print("No matching books found.")
            elif cc == 3:
                break
            else:
                print("Invalid choice")


def user_menu():
    user = User()
    while True:
        print("1. Registration\n2. Login\n3. Exit")
        choice = int(input("Enter your option: "))
        if choice == 1:
            user.regi()
        elif choice == 2:
            user.login()
        elif choice == 3:
            print("Exiting user menu")
            break
        else:
            print("Invalid choice")


while True:
    print("1. ADMIN\n2. USER\n3. EXIT")
    a = int(input("Enter the choice: "))
    if a == 1:
        admin = Admin()
        admin.login()
    elif a == 2:
        user_menu()
    elif a == 3:
        print("Successfully exited")
        break
    else:
        print("Invalid choice")
