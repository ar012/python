for i in range(1, 11):
    print(i)

print("End\n")

# continue
print("Print from 1 to 10 except 5")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
print("End")

print("\nPrint from 1 to 10 except 5, 7, 9")
for j in range(1, 11):
    if j == 5:
        continue
    elif j == 7:
        continue
    elif j == 9:
        continue
    print(j)
print("End")

# break
print("\nPrint from 10 to 20, break from 16")
for i in range(10, 21):
    if i > 15:
        break
    print(i)

# break-continue
print("\nPrint from 10 to 30 except 13, break from 26")
for i in range(10, 31):
    if i == 13:
        continue
    if i == 18:
        continue
    if i > 26:
        break
    print(i)
