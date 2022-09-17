import math

x=float(input("Введіть x:"))
y=float(input("Введіть y:"))

W=float((math.sin(x)-math.cos(y))*4.138*math.log(abs(math.sin((math.pi/4)+(2.31*x))),math.e))

print("W=",W)