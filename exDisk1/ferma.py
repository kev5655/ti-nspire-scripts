from math import floor


print("a^x mod p")

a = int(input("a="))
x = int(input("x="))
p = int(input("p="))


factor = floor(x / (p - 1))
rest = x - ((p-1) * factor)
print(a, "^", p-1, "*", factor, "*", a, "^", rest, " = mod ", p)
print("solution (", a, "^", rest, " = mod ", p, "): ", pow(a, rest, p))
