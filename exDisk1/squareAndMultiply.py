def squareAndMultiply(c, a, m):
    result = []
    q = a
    while q > 0:
        b = 0
        while 2**b < q:
            b += 1
        if 2**b == q:
            result.append(2**b)
            q -= 2**b
        else:
            result.append(2**(b - 1))
            q -= 2**(b-1)
    number = str(a) + " = "
    for i in range(len(result)):
        if i != len(result) - 1:
            number += str(result[i]) + " + "
        else:
            number += str(result[i])
    print(number)
    print()
    interimResults = []
    z = c



    hasPrinted = False
    i = 1
    while i <= result[0]:
        for j in range(len(result) - 1, -1, -1):
            
            if i == result[j]:
                    print(str(c),"^",str(i)," mod ",str(m)," = ",str(z % m)," SOLUTION")
                    hasPrinted = True
                    interimResults.append(z % m)
                
        if(hasPrinted == False):
            print(str(c),"^",str(i)," mod ",str(m)," = ",str(z % m))
        
        else:
            hasPrinted = False
        i = i*2
        z = pow(z, 2) % m
       
    endResult = 1
    for i in range(len(interimResults)):
        endResult *= interimResults[i] % m
    print()
    return str(c) + "^" + str(a) + " mod " + str(m) + " = " + str(int(endResult % m))


print("Square and multiply in the form: a^b mod m")
print("Please enter a")
a = int(input())
print("Please enter b")
b = int(input())
print("Please enter m")
m = int(input())
print()

print(squareAndMultiply(a,b,m))
