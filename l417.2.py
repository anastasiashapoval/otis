import sys
Ax=float(sys.argv[1])
Ay=0
Bx=float(sys.argv[2])
By=0 

AB = ((Bx-Ax)**2 + (By-Ay)**2)**0.5

AC = -Ax*2

print(f"AC = BC = {AC}")
print(f"AB = {AB}")