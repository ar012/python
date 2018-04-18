try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero(0)")
# except ValueError:
#     print("Value error occurred")
# except TypeError:
#     print("Type error occurred")
## OR
except (ValueError, TypeError):
    print("Type or Value error occured")

print("\nException Handling")
try:
    word = "spam"
    print(word/0)
except:
    print("An error occurred")
