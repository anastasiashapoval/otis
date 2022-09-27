import math

def func01(a):
    y=((math.e**(0.9*a+4))+((a+(2*(a**2)))**0.25))/(61*((abs(a+2)+1)))-(9*math.cos((0.7*a)+math.sqrt(a)))
    return(y)

x=float(input("Введіть x: "))
y=func01(x)
print("f(x) = ",y)