import math

def euclid(a, b):
    r = 1
    q = a
    p = b
    lefties = []
    rests = []
    mains = []
    multiplicators = []
    while r != 0:
        r = q % p
        multiplicators.append(math.floor(q/p))
        lefties.append(q)
        mains.append(p)
        rests.append(r)
        q = p
        p = r

    for i in range(0,len(lefties)):
        print(lefties[i]," = ",multiplicators[i]," * ",mains[i]," + ",rests[i])
    return 1

print("ggt(a,b)")
a = int(input("PLease enter a="))
b = int(input("Please enter b="))
euclid(a,b)