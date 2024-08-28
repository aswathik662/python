# l1=[1,2,3,4]
# l2=[5,6,7]
# i=set(l1).intersection(l2)
# print(i)

# a=set()
# print(type(a))

# set={1,2,3,4}
# print(type(set))

# days=set(["mon","tue","wed"])
# print(days)
# print(type(days))
# for i in days:
#     print(i)


# day=set(["mon","tue","wed"])
# print(day)
# day.add("fri")
# print(day)

# m=set(["jan","feb","mar"])
# print(m)
# m.update(["june","july"])
# print(m)

# m=set(["jan","feb","june","oct"])
# print(m)
# m.discard("jan")
# print(m)

# m=set(["jan","feb","mar"])
# print(m)
# m.remove("jan")
# print(m)

# day1={"mon","tue","wed"}
# day2={"thu","fri","sat"}
# print(day1|day2)

# day1={"mon","tue","wed"}
# day2={"mon","tue","sun","fri"}
# print(day1&day2)

day1={"mon","tue","wed"}
day2={"mon","tue"}
day3={"mon","tue","fri","thu"}
print(day1>day2)
print(day1<day2)
print(day1==day2)