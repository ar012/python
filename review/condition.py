# temperature = 35

# if temperature > 30:
#     print("It's warm")
#     print("Drink water")
# print("Done")


age = 20
# if age >= 18:
#   print("Eligible")
# else:
#   print("Not eligible")

# if age >= 18:
#     message = "Eligible"
# else:
#     message = "Not eligible"

# print(message)


message = "Eligible" if age >= 18 else "Not eligible"

# print(message)


high_income = False
good_credit = True

student = False

# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not eligible")


# if high_income or good_credit:
#     print("Eligible")
# else:
#     print("Not eligible")

# if not student:
#     print("Eligible")
# else:
#     print("Not eligible")


if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
