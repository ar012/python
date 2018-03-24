def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("You can't divide by zero(0)")
    except TypeError:
        print("Data type not supported")
    else:
        return result
#    finally:
#        print("iside finally")

x = 10
y = 3
print(divide(x, y))

x = 5
y = 0
print(divide(x, y))

a = "40"
b = "10"
print(divide(a, b))

print("Exception in for loop")
for i in range(10):
    print(i)
#    break
else:
    print("Inside else")