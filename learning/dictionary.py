my_dic = {}

my_marks = {'math': 80, 'bangla': 65, 'english': 70}

print("Obtain marks =", my_marks['english'])


my_marks2 = {'math': [80, 85], 'bangla': [65, 70, 72], 'english': [70, 68]}

print("Obtain marks =", my_marks2['english'])



dic2 = {True: 'Bangladesh'}
print(dic2[True])

dict3 = {1: 'arif', 2: "sharif", 3: "rashed", 4: 'zia'}
print(dict3[3])

dict3[3] = "shahid"
print(dict3[3])

print(dict3)

dict3[5] = "tareq"
print(dict3)

print( 4 in dict3)

print( 6 in dict3)

# use of get
print("\nuse of get in dictionay")
print(dict3.get(5))
print(dict3.get(2))

print(dict3.get(6))

print(dict3.get(7, "7 is not exist in the dictionay dict3"))

