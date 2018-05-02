import re
# Match string that contains NOT ALL capital letters
pattern = r"[^A-Z]"

if re.search(pattern, "a sentence with all lower case letters."):
    print("Match 1")

if re.search(pattern, "A sentence with mixed English letters."):
    print("Matche 2")

if re.search(pattern, "HEADING"):
    # All Capital letters
    # No Match
    print("Match 3")

if re.search(pattern, "HEADING WITH ALL CAPITAL LETTERS"):
    # All capital letters
    # but "spaces" makes it True to NOT ALL Capital
    print("Match 4")