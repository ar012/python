from itertools import count

for i in count(3):
    print(i)
    if i >= 10:
        break

##########
from itertools import accumulate

my_numbers = [1, 2, 3, 4, 5, 6]
accumulated_numbers = accumulate(my_numbers)
list_of_accu_nums = list(accumulated_numbers)
print(list_of_accu_nums)


################
from itertools import takewhile
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_less_equal_six = takewhile(lambda x: x <=6, my_numbers)
filtered_numbers = list(nums_less_equal_six)
print(filtered_numbers)


###########
print("\nUse of product, permutations\n")
from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))