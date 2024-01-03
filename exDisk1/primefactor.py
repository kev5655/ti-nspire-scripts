import math

n = float(input("Enter n="))
k = float(input("Enter start k="))
t = 0
x = 0
it = 0


for i in range(1000):
    it = i
    t = pow(k + i, 2) - n
    sqr = math.sqrt(t)
    isInt = sqr == math.floor(sqr)
    if isInt:
        x = i
        break

print(f"iterationen {it}")
print(f"({k} + {x})^2 - {n} = {t} = {sqr}^2")
