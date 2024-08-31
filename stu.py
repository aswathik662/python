a={}
b=int(input("enter the size\n"))
for i in range(b):
    c={}
    id=int(input("enter the id\n"))
    name=input("enter name\n")
    age=int(input("enter age\n"))
    mark1=int(input("enter mark1\n"))
    mark2=int(input("enter mark2\n"))
    mark3=int(input("enter mark3\n"))
    c["name"]=name
    c["age"]=age
    c["mark1"]=mark1
    c["mark2"]=mark2
    c["mark3"]=mark3
    a[id]=c

li=list(c.items())
print(li)
