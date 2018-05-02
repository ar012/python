import re
## meta character dot(.)
print("\nUse of meta character dot(.)")
pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Mathc 3")

## meta character ^ and $
print("\nUse of meta character ^ and $")
import re
pattern2 = r"^wr.te$"

if re.match(pattern2, "write"):
    print("Match 1")

if re.match(pattern2, "wrote"):
    print("Match 2")

if re.match(pattern2, "writer"):
    print("Match 3")



