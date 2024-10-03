<<<<<<< HEAD
# n=int(input("enter a number:"))
# def fun(n):
#  if n==0:
#     return 0
#  else: 
#     return(n+fun(n-1))
# print(fun(n))

# n=[]
# p=int(input("enter the size:"))
# for i in range(p):
#     num=int(input("enter the elements:"))
#     n.append(num)
# def fun(num):
#     if num==0:
#       return 0
#     else:
#       return(num+fun(num-1))
# print(fun(num))



# n=input("enter a string:")
# vowels = 'aeiouAEIOU'
# def cv(n):
#     count = 0
#     for char in n:
#         if char in vowels:
#             count += 1
#     return count
# for i in (n):
#     if i in vowels:
#       print(i)
# print(cv(n))


# 
# 
# def fib(i):
#       if(i==0):
#          return 0
#       elif(i==1):
#          return 1
#       else:
#          return fib(i-1)+fib(i-2)
# n=int(input("enter the number:"))
# for i in range(10):
#    print(fib(i))
# 
# 
# 
# 
# # 
# s1=input("enter 1st string:")
# s2=input("enter 2nd string:")
# def fun(s1,s2):
#      a=len(s1)
#      b=len(s2)
#      if str(s1)== str(s2) and sorted(str(a))==sorted(str(b)) :
#       print("the stringa are anagram")
#      else:
#         print("The strings are not anagrams")
# fun(s1,s2)

# n=input("enter a string: ")
# def fun(n):
#     p=n.split()
#     return len(p)
# print(fun(n))


# 

n = input("Enter a string: ")
v = "aeiouAEIOU" 
count=0  
vowels=[]  
for i in n:
    if i in v:
        count += 1
        vowels.append(i)  


print("Vowels:", vowels)
print("Number of vowels:", count)  

=======
# n=int(input("enter a number:"))
# def fun(n):
#  if n==0:
#     return 0
#  else: 
#     return(n+fun(n-1))
# print(fun(n))

# n=[]
# p=int(input("enter the size:"))
# for i in range(p):
#     num=int(input("enter the elements:"))
#     n.append(num)
# def fun(num):
#     if num==0:
#       return 0
#     else:
#       return(num+fun(num-1))
# print(fun(num))



# n=input("enter a string:")
# vowels = 'aeiouAEIOU'
# def cv(n):
#     count = 0
#     for char in n:
#         if char in vowels:
#             count += 1
#     return count
# for i in (n):
#     if i in vowels:
#       print(i)
# print(cv(n))


# 
# 
# def fib(i):
#       if(i==0):
#          return 0
#       elif(i==1):
#          return 1
#       else:
#          return fib(i-1)+fib(i-2)
# n=int(input("enter the number:"))
# for i in range(10):
#    print(fib(i))
# 
# 
# 
# 
# # 
# s1=input("enter 1st string:")
# s2=input("enter 2nd string:")
# def fun(s1,s2):
#      a=len(s1)
#      b=len(s2)
#      if str(s1)== str(s2) and sorted(str(a))==sorted(str(b)) :
#       print("the stringa are anagram")
#      else:
#         print("The strings are not anagrams")
# fun(s1,s2)

# n=input("enter a string: ")
# def fun(n):
#     p=n.split()
#     return len(p)
# print(fun(n))


# 

n = input("Enter a string: ")
v = "aeiouAEIOU" 
count=0  
vowels=[]  
for i in n:
    if i in v:
        count += 1
        vowels.append(i)  


print("Vowels:", vowels)
print("Number of vowels:", count)  

>>>>>>> dc0e1ae4da810d941227dbee9087de054f1803fe
    