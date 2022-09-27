import math
def func01 (x):
    return math.log(abs(2*x+7), 5) + (x-4)**(1/3)
    
a=int(input("a = "))
b=int(input("b = "))
h=int(input("h = "))

for i in range(a,b,h):
    print(func01(i))