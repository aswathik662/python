# n=5
# for i in range (n):
#         for j in range(n):
#                 print("* " ,end=" ")
#         print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("* ",end=" ")
#     print()
 

# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("* ",end=" ")
#     print()

n=5
for i in range (n):
        for k in range(i+1):
                print(" ",end=" ")
        
        for j in range(n):
                print(" * " ,end="")
        
        print()

        
# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# n = int(input("Enter the number: "))
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1:
#             print("-", end="")
#         elif j == 0 or j == n-1:
#             print("|", end="")
        
#         else:
#             print(" ", end="")
#     print()

# n = int(input("Enter a number: "))
# for i in range(n):
#     for j in range(n):
#        if (i+j==2)  or  (j-i == 2) or (i+j==6) or (i-j==2):
#            print(" *",end="")
#        else:
#            print(" ",end="")
#     print()

# n=int(input("enter the number: "))
# for i in range(n):
#     for j in range(n):
#         if (i+j==3):
#             print("*",end="")
#         else:
#             print(" ",end="")
#             print() 