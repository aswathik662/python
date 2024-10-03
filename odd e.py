# l=[]
# s=[]
# z=[]
# for i in range(1,11):
#      if i%2==0:
#         s.append(i)
#      else:
#       l.append(i)
# z.append(s)
# z.append(l) 
# print(z)  


# {"13579":"246810"}
d={}
odd=""
even=" "
for i in range(1,11):
    if i%2==0:
        even=even+str(i)
    else:
        odd=odd+str(i)
# d={odd:even}
# d[odd]=even
# print(d)

# print("{"+odd"+ :"+even+"}")
# print(type())

# dict={x:y for x in range(11) if x%2!=0 for y in range(11) if y%2==0}
# dict.append("x")
# print(dict)
#