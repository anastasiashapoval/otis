import math
def func01(a,b):
    W=float((math.sin(a)-math.cos(b))*4.138*math.log(abs(math.sin((math.pi/4)+(2.31*a))),math.e))
    return(W)
x=float(input("Введіть x:"))
y=float(input("Введіть y:"))
W=func01(x,y)
print("W = ",W)