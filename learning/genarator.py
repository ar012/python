n = 10
def my_iterable():
    i = n
    while i > 0:
        yield i
        i -= 1
for i in my_iterable():
    print(i)

###########
print("\nEven numver genarator")

def even_numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

even_num_list = list(even_numbers(11))
print(even_num_list)