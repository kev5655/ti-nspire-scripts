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

def teilerfremd(a):

    results = []

    for i in range(1,a):
        if(ggT(i,a) == 1):
            results.append(i)

    return results

print("Calculates the number of teilerfremde numbers from n")
a = int(input("Enter n:"))
print(teilerfremd(a))