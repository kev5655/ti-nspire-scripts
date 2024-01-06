# ToDo wofür gilt 48 ≡ 33 (mod m)

def multiInverse(a, b):
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
a = int(input("Please enter a="))

m = int(input("Please enter m="))

result = multiInverse(a, m)

if result == -1:
    print("ggT is not 1")

else:
    print("Multiplicative Inverse is :", result)
