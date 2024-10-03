n=int(input("enter the size:"))
a=[]
for i in range (n):
    e=int(input("enter the elements:"))
    a.append(e)
print(a)
p={}
for i in  a:
    if i in p:
        p[i]+=1
    else:
        p[i]=1
print(p) 
l=[]

for i in p:
    if p[i]==1:
        l.append(i)
print(l)
d=max(l)
print(d)
       


    
        