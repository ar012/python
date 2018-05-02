import re

pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
    print("Match 1")

match = re.match(pattern, "?! ?!")
if match:
    print("Match 2")

match = re.match(pattern, "abc cde")
if match:
    print("Match 3")

#########################
print("\nUse of \d   \s  \w   \D:\n")
# \d \s \w      \D

pattern2 = r"(\D+\d)"

match = re.match(pattern2, "Hi 999!")
if match:
    print("Match 1")

match = re.match(pattern2, "1, 23, 456!")
if match:
    print("Match 2")

match = re.match(pattern2, " ! $?")
if match:
    print("Match 3")

###############
pattern3 = r"(\d+\d)"

match = re.match(pattern3, "10 asd")
if match:
    print("Match 4")

pattern3 = r"(\s+\d)"

match = re.match(pattern3, "  45asd123")
if match:
    print("Match 5")