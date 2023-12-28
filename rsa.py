import math

# ToDo validate is n smaller than m
# ToDo is gcd()


def main():
    p = val_input("Enter prime p=")
    q = val_input("Enter prime q=")

    n = val_input("Enter prime factor n=")

    e = val_input("Enter pub key e=")
    d = val_input("Enter priv key d=")

    m = val_input("Enter message m=")
    c = val_input("Enter encrypted msg c=")

    if p is None and q is None:
        (p, q) = factorize(n)
        print(f"factorized p={p} q={q}")
    elif p is None:
        p = n / q
        print(f"p={p}")
    elif q is None:
        q = n / p
        print(f"q={q}")

    if n is None:
        n = p * q

    if e is None:
        if d is None:
            print(f"Error d is None d={d}")
            exit
        e = wrap_extended_euclaid(d, calc_phi(p, q))
    if d is None:
        if e is None:
            print(f"Error e is None e={e}")
            exit
        d = wrap_extended_euclaid(e, calc_phi(p, q))
    print(f"calc e={e}, d={d}")

    if c is None and m is None:
        print("Error c and m is None")
        exit

    if c is None:
        c = pow(m, e, n)
    if m is None:
        m = pow(c, d, n)

    print(f"m={m} c={c} e={e} d={d} n={n} p={p} q={q}")


def factorize(n: int):
    k = int(math.ceil(math.sqrt(n)))
    for i in range(1000):
        t = pow(k + i, 2) - n
        sqr = math.sqrt(t)
        if sqr == math.floor(sqr):  # check is ganze Zahl
            p = (k + i) + int(sqr)
            q = (k + i) - int(sqr)
            return (p, q)
    print(f"Error no factor found for n={n}")


def wrap_extended_euclaid(a: int, n: int) -> int:
    res = extended_euclaid(a, n)
    b = res[1]
    while b < 0:
        b += n
    return b


def extended_euclaid(a: int, b: int) -> tuple:
    assert (math.gcd(a, b) == 1.0)
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclaid(b % a, a)
        return gcd, y - (b // a) * x, x


def calc_phi(p: int, q: int) -> int:
    return (p - 1) * (q - 1)


def val_input(prompt: str):
    inp = input(prompt)
    if inp.strip() == '':
        return None
    try:
        number = int(inp)
        return number
    except ValueError:
        print(f"Error -> {prompt} is a string")


if __name__ == "__main__":
    main()
