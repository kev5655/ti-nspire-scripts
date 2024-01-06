from math import floor

a = int(input("a="))
b = int(input("b="))

store = []


def euclaid(a: int, b: int):
    if (b > a):
        a, b = b, a

    factor = floor(a/b)
    rest = a - b * factor
    if (rest == 0):
        return {
            "result": a,
            "factor": factor,
            "base": b,
            "rest": rest
        }

    store.append({
        "result": a,
        "factor": factor,
        "base": b,
        "rest": rest
    })

    euclaid(b, rest)

    return store


def extended_euclaid():
    exit


x = euclaid(a, b)

for i in x:
    print(i)
