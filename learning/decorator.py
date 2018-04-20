def my_decorator(func):
    def decorate():
        print("----------")
        func()
        print("----------")
    return decorate

def print_raw():
    print("Clear Text")

# decorated_function = my_decorator(print_raw)
# decorated_function()

print_raw = my_decorator(print_raw)
print_raw()

# @decorator
print("\nmy_decorator apply on function\n")

# def print_text():
#     print("Hello World!")

@my_decorator
def print_text():
    print("Hello World!")
print_text()