<<<<<<< HEAD

# right triangle
# n=int(input("enter the number:"))
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()
# inverted
# n=int(input("enter the number:"))
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print("*",end=" ")
#     print()

# diamond
n=int(input("enter the number:"))
# for i in range(n-1):
#         for j in range(i,n):
#             print(" ",end=" ")
#         for k in range(i+1):
#             print(" * ",end=" ")
#         print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(i,n):
        print(" * ",end=" ")
    print()

# inverted diamond
# n=int(input("enter the number:"))
# for i in range(n-1):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print(" * ",end=" ")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print(" * ",end=" ")
#     print()

# hollow tri
# n=int(input("enter the number:"))
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         if k==i or k==0 or i==n-1:
#          print(" * ",end=" ")
#         else:
#            print("    ",end="")
#     print()

# hollow inv
# n=int(input("enter the number:"))
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(n-i):
#         if k==n-i-1 or k==0 or i==0:
#             print(" * ",end=" ")
#         else:
#            print("    ",end="")
#     print()

# number
# n=int(input("entter the number:"))
# p=1
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#         p+=1
#     print()
# 
# 
# n=int(input("enter the number:"))
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==i or i==0:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
=======
# n=int(input("enter the number:"))
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()

# n=int(input("enter the number:"))
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print("*",end=" ")
#     print()
# n=int(input("enter the number:"))
# for i in range(n-1):
#         for j in range(i,n):
#             print(" ",end=" ")
#         for k in range(i+1):
#             print(" * ",end=" ")
#         print()


# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print(" * ",end=" ")
#     print()

# 
# n=int(input("enter the number:"))
# for i in range(n-1):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print(" * ",end=" ")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print(" * ",end=" ")
#     print()

# n=int(input("enter the number:"))
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for k in range(i+1):
#         if k==i or k==0 or i==n-1:
#          print(" * ",end=" ")
#         else:
#            print("    ",end="")
#     print()


# n=int(input("enter the number:"))
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(n-i):
#         if k==n-i-1 or k==0 or i==0:
#             print(" * ",end=" ")
#         else:
#            print("    ",end="")
#     print()

n=int(input("entter the number:"))
p=1
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    print()
>>>>>>> dc0e1ae4da810d941227dbee9087de054f1803fe
