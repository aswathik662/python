<<<<<<< HEAD
class Student:
    l = []

    def add(self):
        c = int(input("Enter roll number: "))
        
        if any(student[1] == c for student in self.l):
            print("Roll number already exists.")
            return
        
        b = input("Enter your name: ")
        d = int(input("Enter mark1: "))
        e = int(input("Enter mark2: "))
        f = int(input("Enter mark3: "))
        ll = [b, c, d, e, f]
        self.l.append(ll)
        print("Student added successfully.")

    def view(self):
        if not self.l:
            print("No students to display.")
        else:
            for i in self.l:
                print("\nName:", i[0])
                print("Roll Number:", i[1])
                print(f"Marks in three subjects: {i[2]}, {i[3]}, {i[4]}")
        
    def up(self):
        g = int(input("Enter the roll number to update: "))
        flag = 0
        for i in self.l:
            if i[1] == g:
                flag = 1
                i[2] = int(input("Enter new mark1: "))
                i[3] = int(input("Enter new mark2: "))
                i[4] = int(input("Enter new mark3: "))
                print("Updated successfully.")
                break
        if flag == 0:
            print("Student does not exist.")

    def cal(self):
        gg = int(input("Enter roll number to calculate average: "))
        for i in self.l:
            if i[1] == gg:
                average = (i[2] + i[3] + i[4]) / 3
                print(f"\nName: {i[0]}\nAverage mark: {average:.2f}")
                return
        print("Student does not exist.")

    def main(self):
        while True:
            print("\nMenu:")
            print("1. Add")
            print("2. View all")
            print("3. Update")
            print("4. Calculate average mark")
            print("5. Exit")
            a = int(input("Enter your option: "))
            if a == 1:
                self.add()
            elif a == 2:
                self.view()
            elif a == 3:
                self.up()
            elif a == 4:
                self.cal()
            elif a == 5:
                break
            else:
                print("Invalid option. Please try again.")


stu= Student()
stu.main()
=======
class Student:
    l = []

    def add(self):
        c = int(input("Enter roll number: "))
        
        if any(student[1] == c for student in self.l):
            print("Roll number already exists.")
            return
        
        b = input("Enter your name: ")
        d = int(input("Enter mark1: "))
        e = int(input("Enter mark2: "))
        f = int(input("Enter mark3: "))
        ll = [b, c, d, e, f]
        self.l.append(ll)
        print("Student added successfully.")

    def view(self):
        if not self.l:
            print("No students to display.")
        else:
            for i in self.l:
                print("\nName:", i[0])
                print("Roll Number:", i[1])
                print(f"Marks in three subjects: {i[2]}, {i[3]}, {i[4]}")
        
    def up(self):
        g = int(input("Enter the roll number to update: "))
        flag = 0
        for i in self.l:
            if i[1] == g:
                flag = 1
                i[2] = int(input("Enter new mark1: "))
                i[3] = int(input("Enter new mark2: "))
                i[4] = int(input("Enter new mark3: "))
                print("Updated successfully.")
                break
        if flag == 0:
            print("Student does not exist.")

    def cal(self):
        gg = int(input("Enter roll number to calculate average: "))
        for i in self.l:
            if i[1] == gg:
                average = (i[2] + i[3] + i[4]) / 3
                print(f"\nName: {i[0]}\nAverage mark: {average:.2f}")
                return
        print("Student does not exist.")

    def main(self):
        while True:
            print("\nMenu:")
            print("1. Add")
            print("2. View all")
            print("3. Update")
            print("4. Calculate average mark")
            print("5. Exit")
            a = int(input("Enter your option: "))
            if a == 1:
                self.add()
            elif a == 2:
                self.view()
            elif a == 3:
                self.up()
            elif a == 4:
                self.cal()
            elif a == 5:
                break
            else:
                print("Invalid option. Please try again.")


stu= Student()
stu.main()
>>>>>>> dc0e1ae4da810d941227dbee9087de054f1803fe
