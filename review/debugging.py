# def multipy(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("Start")

# print(multipy(1, 2, 3))


# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#       return "FizzBuzz"
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#       return "Buzz"
#     return input

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else:
        return input


print(fizz_buzz(30))
