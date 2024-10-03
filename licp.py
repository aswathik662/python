class Book:
    books = []

    def __init__(self, book_id, title, author, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def add(self):
        Book.books.append(self)

    def update(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity

    @classmethod
    def delete(cls, book_id):
        for book in cls.books:
            if book.book_id == book_id:
                cls.books.remove(book)
                return True
        return False

    @classmethod
    def display(cls):
        return cls.books

    def __str__(self):
        return f"{self.book_id} {self.title} {self.author} {self.quantity}"


class Admin:
    credentials = {"a": "1"}

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in self.credentials and self.credentials[username] == password:
            print("Successfully logged in")
            self.manage_books()
        else:
            print("Invalid credentials")

    def manage_books(self):
        while True:
            print("1. Add Book\n2. Update Book\n3. Delete Book\n4. Display All Books\n5. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                book_id = int(input("Enter book ID: "))
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                quantity = int(input("Enter book quantity: "))
                new_book = Book(book_id, title, author, quantity)
                new_book.add()
            elif choice == 2:
                book_id = int(input("Enter book ID: "))
                for book in Book.books:
                    if book.book_id == book_id:
                        title = input("Enter new book title: ")
                        author = input("Enter new book author: ")
                        quantity = int(input("Enter new book quantity: "))
                        book.update(title, author, quantity)
                        print("Book updated successfully")
                        break
                else:
                    print("Book not found")
            elif choice == 3:
                book_id = int(input("Enter book ID: "))
                if Book.delete(book_id):
                    print("Book deleted successfully")
                else:
                    print("Book not found")
            elif choice == 4:
                for book in Book.display():
                    print(book)
            elif choice == 5:
                print("Exiting")
                break
            else:
                print("Invalid choice")


def main():
    while True:
        print("1. ADMIN\n2. USER\n3. EXIT")
        choice = input("Enter your choice: ")
        if choice == '1':
            admin = Admin()
            admin.login()
        elif choice == '2':
            print("User functionality is not implemented yet.")
        elif choice == '3':
            print("Successfully exited")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
