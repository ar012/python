tuple0 = ()

tp = (10, 41, 32)
print(tp)

tp = ("arithmetic", 'geometry', 'algebra', 'trigonometry')
print(tp)

print("1st entry of this tuple is", tp[0])
print("2nd entry of this tuple is", tp[1])
print("4th entry of this tuple is", tp[3])


position =  ((2, 5, 7, 6), [8, 'apple'], {"rank": 2, "designation": 'admin'})

print(position)
print(position[0])
print(position[2]["designation"])

print("\ntuple unpacking")
num = (2, 4, 6)
x, y, z = num
print(x)
print(y)
print(z)

print("\nmultiple elements assign in single variable")
a, *b, c, d = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(a)
print(b)
print(c)
print(d)
