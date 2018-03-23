list1 = range(10)

list2 = range(100, 5)

list3 = range(20, 80, 2)

print("break in for loop")

for i in range(100):
    print(i)
    if i > 50:
        break

print("continue in for loop")
for i in range(20):
    if i < 10:
        continue
    print(i)

