import re
pattern = r"Bangladesh"

if re.search(pattern, "There is country named Bangladesh in south asia!"):
    print("Match Found")
else:
    print("No match")

pattern = r"bangla"
print(re.findall(pattern, "Bangladeshi bangla and indian bangla are different."))

###########
import re
pattern2 = r"bin"

match = re.search(pattern2, "combination")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())