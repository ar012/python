num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = []
for num in num_list:
    if num % 2 == 0:
        even_num.append(num)
print(even_num)


print("\nList comprehension for even number from a list")

even_num_list = [even for even in num_list if even % 2 == 0]
print(even_num_list)

# #OR
# print("\nList comprehension for even number from a list")
# even_num_list = [
#     even
#     for even in num_list
#         if even % 2 == 0
# ]
# print(even_num_list)


print("\nList comprehension for odd number from 1 to 50")
new_list = [n for n in range(1, 51) if n % 2 !=0]
print(new_list)