# a = 10
# b = 0
# print(a/b)
# print("I did it")

try:
    a = 100
    b = int(input("Enter a divisor to divide 100: "))
    # b = input("Enter a divisor to divide 100: ")
    print(a/b)
except ZeroDivisionError:
    print("You entered 0 which is not permitted")
except ValueError:
    print("Value error occurred")


