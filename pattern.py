num=int(input("enter number of rows: "))

def alpha(num):
    for i in range(num):
        for k in range(num-i-1):
            print(" ",end="")
        for j in range(i+1):
            print(chr(65+j),end=" ")
        print()
alpha(num)

