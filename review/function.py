# def greet():
#     print("Hi there")
#     print("Welcome aboard")


# greet()


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 5))


# def multiply2(*numbers):
#     print(numbers)


# multiply2(2, 3, 4, 5)


# def save_user(**user):
#     print(user)
#     # print(user["name"])


# save_user(id=1, name="AR", email="a.razzak660@gmail.com")

message = "Hello"

def greet():
    global message
    message = "welcome"


print(message)
