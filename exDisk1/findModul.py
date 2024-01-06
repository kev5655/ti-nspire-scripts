def findModul(a, b):
    teiler = []
    for i in range(1, a - b + 1):
        if (a - b) % i == 0:
            teiler.append(i)
    
    endResults = []
    for j in teiler:
        for q in range(0, a + 1):
            if a - (q * j) == b:
                endResults.append(q)

    return endResults


print("a = b mod m")
print("Please enter a=")
a = int(input())
print("Please enter b=")
b = int(input())

print("m = ",findModul(a,b))