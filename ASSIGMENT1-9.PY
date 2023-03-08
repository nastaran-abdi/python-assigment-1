a=(input("please enter your name"))
b=float(input("please enter your weight(kg)"))
c=float(input("please enter your tall(m)"))
bmi=(b)/c**2
print(bmi)
if  bmi<18.5:
   print("under weight")
elif  18.5<bmi<24.9:
   print("normal")
elif  25<bmi<29.9:
   print("over weight")
elif  30<bmi<34.9:
   print("obese")
elif   bmi>35:
   print("EXTERMLY OBESE")
