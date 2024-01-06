from math import sqrt, ceil, floor

n = int(input("Enter n="))


def primefactor(n: int) -> tuple:
    k = int(ceil(sqrt(n)))
    for i in range(1000):
        print(i)
        t = pow(k + i, 2) - n
        sqr = sqrt(t)
        if sqr == floor(sqr):  # check is ganze Zahl
            p = (k + i) + int(sqr)
            q = (k + i) - int(sqr)
            print("factorized p=" + str(p) + " q=" + str(q))
            print("--("+str(k)+" + " +
                  str(i) + ")^2 - " + str(n) + " = " + str(t) + " => sqrt(" + str(t) + ") = " + str(floor(sqr)))
            print("--" + str(k + i) + "^2 - " + str(t) + "^2 = " + str(n) + "")
            print("--(" + str(k + i) + " + " + str(floor(sqr)) +
                  ") * (" + str(k + i) + " - " + str(floor(sqr)) + ") = " + str(n))
            return (p, q)


(p, q) = primefactor(n)
if p == None or q == None:
    print("Error no factor found for n=" + str(n))
