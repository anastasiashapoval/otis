import sys
Ax=float(sys.argv[1])
Ay=float(sys.argv[2])
Bx=float(sys.argv[3])
By=float(sys.argv[4])

AB = ((Bx-Ax)*2 + (By-Ay)*2)*0.5

AC = -Ax*2

print(f"AB = BC ={AB}")
print(f"AC = {AC}")