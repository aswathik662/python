h=int(input("enter your height"))
w=int(input("enter your weight"))
bmi=w/h*2
if(bmi<18.5):
    print("underweight")
elif(18.5<=bmi<24.9):
        print("normal weight")
elif(25<=bmi<29.9):
      print("overweight")
else:
      print("obese")


