try:
    print("Hello")
    print(10 / 0)
except ZeroDivisionError:
    print("Divided by zero")
    print(Unknown_var)
finally:
    print("This code will run no matter what")