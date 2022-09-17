import math
x=float(input("Введіть x:"))

f=float(((math.e**(0.9*x+4))+((x+(2*(x**2)))**0.25))/(61*((abs(x+2)+1)))-(9*math.cos((0.7*x)+math.sqrt(x))))


print("f(x)=",f)