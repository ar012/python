def make_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(make_twice(add_five, 10))

# Pure function
print("\nPure function")

def my_pure_function(a, b):
    c = (2*a) + (2*b)
    return c
print(my_pure_function(5, 10))

# Impure function
print("\nImpure function")

my_list = []
def my_impure_function(arg):
    my_list.append(arg)

my_impure_function(5)
print(my_list)

# lambda e.g lambda x,y: x+y
print("\nLambda")

# def fn(x):
#     return x*2
# print(fn(3))

print((lambda x: x*2)(3))

def my_function(func, arg):
    return func(arg)
print(my_function(lambda x: 2*x, 5))

########
print((lambda x,y: x+2*y)(2,3))
