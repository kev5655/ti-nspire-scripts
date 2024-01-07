from math import floor

a = 50  # int(input("a="))
b = 80  # int(input("b="))

val_mapper = {
    str(a): "a",
    str(b): "b"
}
# val_mapper = [10000]
# val_mapper[a] = "a"
# val_mapper[b] = "b"


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


def extended_euclaid(store):
    for x in store:
        print(x["rest"], "=", x["result"], "-", x["base"])
        res = val_mapper[str(x["result"])]
        base = val_mapper[str(x["base"])]
        val_mapper[str(x["rest"])] = "(" + str(res) + "-" + str(base) + ")"
        alge = str(res) + "-" + str(base)
        # if (alge.__contains__("(")):
        #     (a, b) = alge.split("(")
        #     if (a.__contains__("-")):
        #         alge = solveBrackets("-", "(" + b)
        #     else:
        #         alge = solveBrackets("+", "(" + b)
        #     alge = [*a][0] + alge
        # if (alge.count("a") > 1 or alge.count("b") > 1):
        # alge = simplify_expression(alge)

        print(str(x["rest"]) + "=" + alge)

    exit


def solveBrackets(sign: str, alge: str):
    alge = alge.replace("(", "").replace(")", "")
    print(alge)
    if (alge.__contains__("-")):
        (a, b) = alge.split("-")
        b = "-" + b
    else:
        (a, b) = alge.split("+")
        b = "+" + b

    if (sign == "-"):
        a = sign + a
        if ([*b][0] == "-"):
            b = "+" + [*b][1]
        else:
            b = "-" + [*b][1]
        return a + b


# def simplify_expression(expr):
#     terms = expr.replace('-', '+-').split('+')
#     term_dict = {}

#     for term in terms:
#         if term:
#             # Identify the coefficient and variable
#             if term[-1].isalpha():
#                 var = term[-1]
#                 coef = term[:-1]
#                 coef = int(coef) if coef != '-' else -1
#             else:
#                 var = ''
#                 coef = int(term)

#             # Combine like terms
#             if var in term_dict:
#                 term_dict[var] += coef
#             else:
#                 term_dict[var] = coef

#     # Construct simplified expression
#     simplified_expr = ''
#     for var, coef in term_dict.items():
#         if coef == 0:
#             continue
#         elif coef == 1 and var:
#             simplified_expr += '+' + var
#         elif coef == -1 and var:
#             simplified_expr += '-' + var
#         else:
#             simplified_expr += ('+' if coef > 0 else '') + str(coef) + var

#     return simplified_expr.lstrip('+')

# print(solveBrackets("-", "(a-b)"))


store = euclaid(a, b)
for i in range(len(store)):
    print(store[i])
print(val_mapper)
extended_euclaid(store)
