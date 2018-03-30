# list slice

marks = [0, 1, 2, 3, 4, 5, 6, 7, 50, 30, 20]
good_marks = marks[5:7]
avg_marks = marks[3: 5]
best_marks = marks[8:]
low_marks = marks[:4]

print(marks)
print(low_marks)
print(good_marks)
print(avg_marks)
print(best_marks)

# jump
print(marks[3:10:2])
print(marks[3::3])


# negative index
print(marks[-1])
print(marks[2:-3])
print(marks[1:-1])

# revers list
print("\nrevers list of the root list")
revers = marks[: : -1]
print(revers)

# list functions
print("\nList functions")
print("Maximum value of the list:", max(marks))
print("Minimum value of the list:", min(marks))
print("Summation of the values of the list:", sum(marks))