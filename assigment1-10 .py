a = (input("please enter your name"))
b = (input("please enter your family"))
c = float(input("please enter first grade"))
d = float(input("please enter second garde"))
e = float(input("please enter third garde"))
average = (c + d + e) / 3
print(average)
if average > 17 or average == 17:
    print("great")
elif 17 < average < 12  or average == 12:
    print("good")
elif average < 12:
    print("fail")
