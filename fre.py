a=int(input("enter the size:"))
l=[]
for i in range (a):
    b=int(input("enter the elements:"))
    l.append(b)
print(l)
d={} 
for j in l:
    if j in d:
        d[j]+=1
    else:
        d[j]=1
print(d)
