vowels = 'aeiou'
sentence = 'I am awesome!'

filter_letters = []
for letter in sentence:
    if letter not in vowels:
        filter_letters.append(letter)

print(''.join(filter_letters))


sentence = "We will conquare"

for letter in sentence:
    print(letter)

# list comprehension
print("\nUsing list comprehension:")

vowels = 'aeiou'
sentence = 'I am awesome!!!'

filter_letters = ''.join(letter for letter in sentence if letter not in vowels)
print(filter_letters)