def fnc(x, y, z=None):
    x = x*x
    y = y*y
    if z is None:
        z = []

    return (x, y, z)
#print(fnc(10, 20, 30))

x, y, z = fnc(10, 20)

print('x =', x)
print('y =', y)
print('z =', z)