num_set = {1, 2, 3, 4, 5}
word_set = {"mango", "banana", "orange"}
subjects = set(["math", "bangla", "english"])

print(1 in num_set)
print("mango" not in word_set)

print(subjects)

print(set())

# duplicate elements
nums = {1, 2, 3, 5, 1, 2, 6, 3, 10}

print(nums)

# To add a element to a set
nums.add(9)
print(nums)

# To remove a element from a set
nums.remove(6)
print(nums)

li = [1, 2, 3, 4, 5, 6, 7, 0, 7, 5]
list = list(set(li))
print(list)

# Set Operations
print("\nSet Operations\n")
a = {1, 2, 3, 4, 8}
b = {5, 3, 7, 8, 10}

# Union of sets
set_union = a | b
print("Union of a and b =", set_union)

# Intersection of sets
set_intersection = a & b
print("Intersection of a and b =", set_intersection)

# difference of sets
set_diff = a - b
print("Diff from a to b =", set_diff)

set_diff2 = b - a
print("Difference from b to a =", set_diff2)

# symmetric difference
# set_sym_diff = a ^ b
# print(Sym_Diff from a to b =", set_sym_diff)