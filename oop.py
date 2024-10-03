# class Employee:
#     id=10
#     name="abs"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp=Employee()
# emp.display()

# class Employee:
#     id=1
#     name="john"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
#         emp=Employee()
#         del emp.name
#         del emp.id
       
#         emp.display()

# class Car:
#     def __init__(self, modelname, year):
#         self.modelname = modelname
#         self.year = year

#     def display(self):
#         print(self.modelname, self.year)

# c1 = Car("ss", 2020)
# c1.display()


# class Employee:
#     def __init__(self,name,id):
#         self.id=id
#         self.name=name
#     def display():
#         print("id:%d\nName:%s"%(self.id,self.name))
# emp1=Employee("ss",100)
# emp2=Employee("shh",101)
# emp2.display()

# class Student:
#     def __init__(self):
#         print("adsk")
#     def show(self,name):
#         print("hello",name)
# Student=Student()
# Student.show("jj")

# class Student:
#     def __init__(self,name):
#         print("djkr")
#         self.name=name
#     def show(self):
#         print("hello",self.name)
# Student=Student("yy")
# Student.show()

# class Student:
#     num=100
#     name="hh"
#     def display(self):
#         print(self.num,self.name)
# st=Student()
# st.display()

# class Student:
#     def __init__(self,name):
#         print("this is a constructor")
#         self.name=name
#     def show(self):
#         print("hello",self.name)
# Student=Student("acd")
# Student.show()

# class Student:
#     def __init__(self, roll_num, name):
#         self.roll_num = roll_num
#         self.name = name

#     def display(self):
#         print(self.roll_num, self.name)

# st = Student(101, "Joseph")
# st.display()

# class Student:
#     def __init__(self):
#         print("The First Constructor")

#     def __init__(self):
#         print("The Second Constructor")

# st = Student()

# class Student:
#     def __init__(self, name, id, age):
#         self.name = name
#         self.id = id
#         self.age = age

# s = Student("Alice", 123, 20)
# setattr(s,"age",23)
# print(getattr(s,'name'))
# print(getattr(s,'age'))
# delattr(s,'age')
# print(s.age)

# class Animal:
#  def speak(self):
#   print("Animal Speaking")
# #child class Dog inherits the base class Animal  
# class Dog(Animal):
#  def bark(self):
#   print("dog barking")
# d=Dog()
# d.bark()
# d.speak()


# class Animal:
#  def speak(self):
#    print("Animal Speaking")
# class Dog(Animal):
#  def bark(self):
#   print("dog barking")
# class DogChild(Dog):
#  def eat(self):
#    print("Eating bread...")
# d = DogChild()
# d.bark()
# d.speak()
# d.eat()
# class Calculation1:
#    def Summation(self,a,b):
#      return a+b
# class Calculation2:
#   def Multiplication(self,a,b):
#      return a*b
# class Derived(Calculation1,Calculation2):
#   def Divide(self,a,b):
#      return a/b
# d=Derived()
# print(d.Summation(10,20))
# print(d.Multiplication(10,20))
# print(d.Divide(10,20))

# class Parent:
# 	def func1(self):
# 		print("This function is in parent class.")

# class Child1(Parent):
# 	def func2(self):
# 		print("This function is in child 1.")

# class Child2(Parent):
# 	def func3(self):
# 		print("This function is in child 2.")
# object1 = Child1()
# object2 = Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()

# class Animal:
#  def speak(self):
#   print("speaking")
# class Dog(Animal):
#  def speak(self):
#   print("Barking")

# d=Dog()
# d.speak()


# class Bank:
#     def getroi(self):
#         return 10

# class SBI(Bank):
#     def getroi(self):
#         return 7

# class ICICI(Bank):
#     def getroi(self):
#         return 8

# b1 = Bank()
# b2 = SBI()
# b3 = ICICI()

# print("Bank Rate of interest:", b1.getroi())
# print("SBI Rate of interest:", b2.getroi())
# print("ICICI Rate of interest:", b3.getroi())

# class Bird:
#     def intro(self):
#         print("There are many types of birds.")

#     def flight(self):
#         print("Most of the birds can fly but some cannot.")

# class Sparrow(Bird):
#     def flight(self):
#         print("Sparrows can fly.")

# class Ostrich(Bird):
#     def flight(self):
#         print("Ostriches cannot fly.")

# obj_bird = Bird()
# obj_sparrow = Sparrow()
# obj_ostrich = Ostrich()
# obj_bird.intro()
# obj_bird.flight()
# obj_sparrow.intro()
# obj_sparrow.flight()
# obj_ostrich.intro()
# obj_ostrich.flight()


# class Base:
#     def __init__(self):
#        self._a = 2
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling protected member of base class:", self._a)
#         self._a = 3
#         print("Calling modified protected member outside class:", self._a)
# obj1 = Derived()
# obj2 = Base()
# print("Accessing protected member of obj1:", obj1._a)
# print("Accessing protected member of obj2:", obj2._a)


# class Base:
#     def __init__(self):
#         self.a = "Hello" 
#         self.__c = "World"  
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         try:
#             print("Calling private member of base class: ")
#             print(self.__c)  
#         except AttributeError:
#             print("Cannot access private member __c directly.")
# obj1 = Base()
# print(obj1.a)  
# try:
#     print(obj1.__c)  
# except AttributeError:
#     print("Cannot access private member __c from outside the class.")

# from abc import ABC, abstractmethod
# class Car(ABC):
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def printDetails(self):
#         pass
#     def accelerate(self):
#         print("Speeding up...")

#     def brake_applied(self):
#         print("Car stopped.")
# class Hatchback(Car):
#     def printDetails(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Year:", self.year)

#     def sunroof(self):
#         print("Not having this feature.")
# class Suv(Car):
#     def printDetails(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Year:", self.year)

#     def sunroof(self):
#         print("Available.")
# car1 = Hatchback("Maruti", "Alto", 2022)
# car1.printDetails()
# car1.accelerate()
