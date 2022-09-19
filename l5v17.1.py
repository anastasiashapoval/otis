import math

def func1(x):
    if x > 3:
        return 2.31 - math.log((math.fabs((x-6))), math.e)
    if 0 <= x <= 3:
        return math.cos(x+3) + math.sin(2*x + math.pi/2) 
    else:
        return 3/x + (math.e**x)/(x**3)
    
for i in range(-5,15):
    try: 
        print(i, func1(i))
    except:
        print(i, "none")