import math

num = input("Введіть чотирицифрове число:  ")
maxv = -1
minv = 10

if int(num[0]) > maxv:
    maxv = int(num[0])
if int(num[0]) < minv:
    minv = int(num[0])
if int(num[1]) > maxv:
    maxv = int(num[1])
if int(num[1]) < minv:
    minv = int(num[1])
if int(num[2]) > maxv:
    maxv = int(num[2])
if int(num[2]) < minv:
    minv = int(num[2])
if int(num[3]) > maxv:
    maxv = int(num[3])
if int(num[3]) < minv:
    minv = int(num[3])


print(minv*maxv, minv, maxv)

