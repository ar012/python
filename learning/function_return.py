# def get_larger(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
# larger_value = get_larger(10, 20)



def get_larger(a, b):
    if a > b:
        return a
    else:
        return b
larger_value = get_larger(10, 50)
print(larger_value)

# bellow return
def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")

print(add_numbers(10, 20))