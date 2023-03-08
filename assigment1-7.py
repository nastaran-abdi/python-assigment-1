import math
print("welcome to nastaran,s calculator")
print("+:sum")
print("-:sub")
print(":*:mul")
print("/:div")
print("sin")
print("log")
print("radical")
print("cos")
print("cot")
print("tan")
print("factorial")
print("d2r:degree to radian")
print("please enter your choice")
op = input()
if op == "+" or op == "-" or op == "*" or op == "/":
  a = float(input("enter first number"))
  b = float(input("enter second number"))
else:
  a = float(input("enter first number"))
if op == "+":
    result = a+b
elif op == "-":
    result = a-b
elif op == "*":
    result = a*b
elif op == "/":
    result = a/b
elif op == "sin":
     result = math.sin(a)
elif op == "cos":
     result = math.cos(a)
elif op == "tan":
     result = math.tan(a)
elif op == "factorial" :
     result = math.factorial(a)
elif op == "cot" :
    result = 1/math.tan(a)
elif op == "degree":
    result = math.degrees(a)
elif op == "/":
 if b == 0:
   print("can not divided by zero")
elif op == "d2r":
     result = (a*math.pi)/180

print(result)


