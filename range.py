# print(range(15))
# print(list(range(15)))
# print(list(range(4,9)))
# print(list(range(5,25,4)))
# for i in range(10):
#     print(i)


# a=input("enter a string\n")
# b=len(a)
# c=""
# for i in range(b):
#     # print(a[i])
#     c=a[i]+c
# print(c)

a={}
b=int(input("enter the size"))
for i in range(b):
    c={}
    id=int(input("enter the id"))
    name=input("enter name")
    place=input("enter place")
    age=int(input("enter age"))
    phone=int(input("enter phone"))
    c["name"]=name
    c["place"]=place
    c["age"]=age
    c["phone"]=phone
    a[id]=c
print(a)

    
    







