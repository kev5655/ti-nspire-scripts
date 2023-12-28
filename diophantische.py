import math


def main():
    print("ax + by = c")
    a = val_input("Enter a=")
    b = val_input("Enter b=")
    c = val_input("Enter c=")
    # if b > a:
    #     (a, b) = (b, a)

    if a is None or b is None or c is None:
        print("Error a b or c is null")
        exit

    c00 = euclaid(a, b, c)

    (_, x00, y00) = extended_euclaid(a, b)
    print(f"x00={x00} y00={y00}")

    (x0, y0) = sum_up(x00, y00, c00, c)
    print(f"First Solution: x0={x0} y0={y0}")

    res = find_all_solutions(x0, y0, c00, b, a)
    print(f"All solution for x,y={res}")


def euclaid(a, b, c) -> int:
    gcd = math.gcd(a, b)
    res = c / gcd
    if res != math.floor(res):
        print("Error diophantine equation has no solution")
        exit

    return gcd


def extended_euclaid(a: int, b: int) -> tuple:
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclaid(b % a, a)
        return gcd, y - (b // a) * x, x  # maybe remove -1


def sum_up(x00: int, y00: int, c00: int, c: int) -> tuple:
    f = int(c / c00)
    return (x00 * f, y00 * f)


def find_all_solutions(x0: int, y0: int, c00: int, b: int, a: int):
    # x
    k_init = (x0 / (b / c00)) * -1
    k_high = math.ceil(k_init)
    k_low = math.floor(k_init)

    test_x = x0 + (b / c00) * k_high

    ks = []
    if (test_x > 0):
        ks.append(k_high)
    else:
        ks.append(k_low)

    # y
    k_init = y0 / (a / c00)
    k_high = math.ceil(k_init)
    k_low = math.floor(k_init)

    test_y = calc_y(y0, c00, a, k_high)

    if (test_y > 0):
        ks.append(k_high)
    else:
        ks.append(k_low)

    ks.sort()
    res = []

    for i in range(ks[0], ks[1]):
        x = calc_x(x0, c00, b, i)
        y = calc_y(y0, c00, a, i)
        res.append((x, y))
    print(f"k={ks}")
    return res


def calc_x(c: int, c00: int, a: int, k: int) -> int:
    return c + (a / c00) * k


def calc_y(c: int, c00: int, b: int, k: int) -> int:
    return c - (b / c00) * k


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
