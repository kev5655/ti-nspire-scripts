def isISBNRight(numbers):
    if len(numbers) != 10:
        print("The length of the ISBN is wrong")
        return False
    else:
        total = 0
        for i in range(1, len(numbers) + 1):
            total += i * int(numbers[i - 1])
        print("Sum mod 11 =", total, "mod 11 =", total % 11)
        return total % 11 == 0


def findMissingNumber(numbers):
    result = []
    index = 0
    for i in numbers:
        if (i == "x"):
            index = numbers.index(i)
            break

    for i in range(0, 10):
        numbers[index] = i
        numbers = [int(x) for x in numbers]
        if (isISBNRight(numbers)):
            result.append(i)
    return result


print("Please enter the ISBN z1,z2,z3,z4,z5,z6,x,z8,z9,z10:")
isbn_input = input()
isbn_numbers = list(isbn_input.split(','))
if "x" in isbn_numbers:
    n = findMissingNumber(isbn_numbers)
    print("The missing number is:", n)
else:
    isbn_numbers = [int(x) for x in isbn_numbers]
    result = isISBNRight(isbn_numbers)
    if result:
        print("The ISBN is correct.")
    else:
        print("The ISBN is not correct.")
