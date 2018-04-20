def make_double(x):
    return x*2

my_marks = [10, 20, 30, 15, 25]
result = map(make_double, my_marks)
print(list(result))



# finding even number from a list:
print("\nfinding even number from a list:")

def is_even(x):
    return x%2 == 0

my_numbers = [1, 2, 3, 4, 10, 12, 13, 15, 16]
result = filter(is_even, my_numbers)
print(list(result))


# Lambda review
print("\nUsing lambda function")
nums = [10, 2, 11, 14, 36, 51]
res = list(filter(lambda x: x%2 == 0, nums))
print(res)

li = list(map(lambda x: x*2, my_marks))
print(li)