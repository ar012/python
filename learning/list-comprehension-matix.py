matrix_id = []
matrix_2d = [[1, 2, 3],
             [4, 5, 6]]
for row in matrix_2d:
    for num in row:
        matrix_id.append(num)

print(matrix_id)


print("\nUsing list comprehension")

matrix_id = [num for row in matrix_2d for num in row]
print(matrix_id)



print("\nUsing list comprehension")

matrix_id = [num**2 for row in matrix_2d for num in row]
print(matrix_id)