# def square(num):
#     return num**2
# ob=square(6)
# print(ob)
# def fun(string):
#     return len(string)
# print(fun("function"))
# print(fun("python"))

# def fun(n1,n2=20):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
# print("passing only one argument")
# fun(30)

# def fun(n1,n2):
#     print("number 1 is:",n1)
#     print("number 2 is:",n2)
# fun(n1=10,n2=20)

# def fun(num):
#     return num**2
# print(fun(52))

# lambda_=lambda argument1,argument2 : argument1+argument2
# print("Value of the function is:",lambda_(20,30))
# print("Value of the function is:",lambda_(40,50))

# def word():
#           string='Python functions tutorial'
#           x=5
#           def number():
#             print(string)
#             print(x)
#           number()
# word()
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 3
print("The factorial of", num, "is", factorial(num))
