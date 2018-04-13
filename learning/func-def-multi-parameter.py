# Defining the function with multiple parameter handling
def make_sum(*args):
    sum = 0
    for num in args: # Here, args is like Tuple which is (10, 20, 30)
        sum += num
    return sum
print(make_sum(10, 20, 30, 50))


print(make_sum(1, 2, 3, 4, 5, 20))

#
# def make_sum(*para):
#     sum = 0
#     for num in para: # Here, args is like Tuple which is (10, 20, 30)
#         sum = sum + num
#     return sum
# print(make_sum(10, 20, 30, 40))


def print_dict(**kwargs):
    print(kwargs)

print_dict(a=1, b=10, manik=50)

# welorganized
def prit_dict(**kwargs):
    for args in kwargs:
        print("{0} : {1}".format(args, kwargs[args]))
print_dict(a=1, b=2, c= 3)


def print_all(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

print_all(10, 20, 30, 40, 50, d=2, b=5, c=15)