## string split

s1 = "a b c"

print(s1.split())

s2 = 'a+b+c'

print(s2.split('+'))

s3 = 'a, b, c, d'
print(s3.split(','))


## list join

li2 = ['a', 'b', '2', '3']

j = '+'.join(li2)

print(j)

#alignment
just = '1000'.rjust(10)
print(just)

print('abc'.zfill(5))