def gen(n):
    i = 0
    while i < n:
        yield i
        i +=1
x = gen(20)

for item in x:
    print(item)

li = [x for x in range(10)]
print(li)

g = (x for x in range(10))

for i in g:
    print(i)


gen = (x for x in range(1, 101))
summation = sum(gen)
print(summation)


