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