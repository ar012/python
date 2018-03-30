fruits = ['apple', 'mango', 'banana', 'orange', 'jackfruit']

print("List of fruits =", fruits)


# stat for loop
# index = 0
# mx_len = len(fruits)
# for fr in fruits:
#     print(fr)
#     fr = index + mx_len

# while loop
print("\nWhile loop start:")

index = 0
mx_len = len(fruits)
while index <= (mx_len -1):
    print(index+1, fruits[index])
    index = index + 1


# for loop
print("\nFor loop in list:")

for fruit in fruits:
    print(fruit)

# another example
print("\nFor loop in range:")
for i in range(10):
    print(i)


