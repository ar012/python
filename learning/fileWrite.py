# file_to_work = open("file.txt", "w")
# file_to_work.write("I am writing!!!")
# file_to_work.close()
#
# file_to_work = open("file.txt", "r")
# print(file_to_work.read())
# file_to_work.close()

#
# file_to_work = open("book.py", "w")
# file_to_work.write("list \nset \ndictionary \nstring")
# file_to_work.close()
#
# file_to_work = open("book.py", "r")
# print(file_to_work.read())
# file_to_work.close()


file_to_work = open("book.py", "w")
is_write_done = file_to_work.write("list \nset \ndictionary \nstring")

if is_write_done:
    print("Yes, {0} byte(s) has been written!".format(is_write_done))
file_to_work.close()

# file_to_work = open("book.py", "r")
# print(file_to_work.read())
# file_to_work.close()