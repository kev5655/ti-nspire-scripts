def multInverse(a, b):
    if ggT(a, b) == 1:
        for i in range(b):
            if (a * i) % b == 1:
                return i
            
    return -1

def ggT(a, b):
    r = 1
    q = a
    p = b
    rests = []
    while r != 0:
        r = q % p
        rests.append(r)
        q = p
        p = r
    return rests[len(rests) - 2]


print("a*b = 1 mod m")
print("Please enter a:")
a = int(input())

print("Please enter m:")
m = int(input())

result = multInverse(a,m)

if result == 1:
    print("ggT is not 1")

else:
    print("Multiplicative Inverse is :",result)