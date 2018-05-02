# named group and non-capturing group
import re

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")

if match:
    print(match.group("first"))
    print(match.groups())

#########################################
## meta character |
print("\nUsing meta character |\n")

pattern2 = r"gr(a|e)y"

match2 = re.match(pattern2, "gray")
if match2:
    print("Gray is fine")
match2 = re.match(pattern2, "grey")
if match2:
    print("Grey is OK also!")

match2 = re.match(pattern2, "griy")
if match2:
    print("No way, what Griy is?!")