None == False
None == 0
None == ""
None == []

a = None
print(a)

# # None return check
# print("\nnew\n")
#
# def my_func():
#     print("Hello")
#
# what_i_got = my_func()
# print(what_i_got)


def my_func(x = None):
    if x:
        return x*x
    else:
        return 0

print("default value =",my_func())

print(my_func(10))