
file_to_work = open("myfile.txt", "r")
print(file_to_work.read())
file_to_work.close()

print("\nOpening file in right way:")

try:
    file_to_work = open("book.py", "r")
    content = file_to_work.read()
    print(content)
finally:
    file_to_work.close()

print("\nOpening file in right way:")

with open("file.txt") as f:
    print(f.read())