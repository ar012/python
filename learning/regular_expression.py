import re
pattern = r"Bangla"

result = re.match(pattern, "Bangladesh")
# print(result)

if result:
    print("Match Found")
else:
    print("No match")

