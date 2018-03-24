def fnc(x, li):
    print('type of x: ',type(x))
    print('type of li: ', type(li))

    x = 500
    li.append(4)

    return x

a = 10
my_list = [1, 2, 3]
print('list before function call: ', my_list)
y = fnc(a, my_list)

print('value of y: ', y)
print('value of a: ', a)

print('list after function call: ', my_list)