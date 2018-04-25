# find out factorial of a number:

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

n = 7
print("Factorial of", n, "is", factorial(n))


#
# def factorial(x):
#     return x * factorial(x-1)
#
# n = 5
# print("Factorial of", n, "is", factorial(n))



# Recursion function direction

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(y):
    return not is_even(y)


print(is_even(12))
print(is_odd(12))

print(is_odd(11))
print(is_even(12))
