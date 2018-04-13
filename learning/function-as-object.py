def add_explanation(line):
    return line + '!'

update_line = add_explanation

print(update_line("Hellow World"))

# print(update_line)

# function as a variable
print("\nfunction as a variable")

def beautify(text):
    return text + '!!!'

#print(beautify("Hello"))

def make_line(func, words):
    return "Hello " + func(words)
print(make_line(beautify, "world"))

