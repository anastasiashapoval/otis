import math
import random
def func01 (x):
    return math.log(abs(2*x+7), 5) + (x-4)**(1/3)
    
a=int(input("a = "))
b=int(input("b = "))
h=int(input("h = "))

list1=[]
for i in range(a,b,h):
    list1.append(func01(i))
print(list1)

list1.sort()

list2=[]
for i in range(a,b,h):
    list2.append(func01(i))

random.shuffle(list2)
print(list2)

