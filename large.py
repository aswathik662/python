<<<<<<< HEAD
n=int(input("Enter a the size of the list:"))
a=[]
c=print("Items in the List:")
for i in range (n):
    c=int(input())
    a.append(c)
print(a)    
for i in range(len(a)):
        for j in range (i+1,len(a)):
                if a[i]>a[j]:
                        a[i],a[j]=a[j],a[i]

print(a[-2])
        

=======
l=[10,5,20,8,30]

for i in range (l):
        if (i<30):
               
               print(i)
    

>>>>>>> dc0e1ae4da810d941227dbee9087de054f1803fe
