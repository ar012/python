# file_working = open("myfile.txt", "w")
# "Bangldes is small country"
# "but it is a beautiful country"
#
# file_working.close()

#
# file_working = open("myfile.txt", "r")
#
# file_working = open("myfile.txt", "a")
#
# ## To open non-text file on write and binary mode
# file_working = open("my_file", "wb")

file_to_work = open("file.txt", "r")
content = file_to_work.read()
print(content)
file_to_work.close()

##############################
print("\nWorking on myfile.txt")

work_file = open("myfile.txt", "r")
just_one_character = work_file.read(1)
print(just_one_character)
remaining_four_characters = work_file.read(4)
print(remaining_four_characters)
rest_of_the_file = work_file.read()
print(rest_of_the_file)
work_file.close()

print("\nWorking on myfile.txt, read line by line")

file_to_work = open("myfile.txt", "r")
lines = file_to_work.readlines()
print(lines)
file_to_work.close()

print("\nReading file line by line using for loop")
file_to_work = open("myfile.txt", "r")

for myline in file_to_work:
    print(myline)

file_to_work.close()