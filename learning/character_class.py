
import re
# one character matching

# A character set containing all vowels
pattern = r"[aeiou]"

# Lets check whether a word got a vowel in it or not
if re.search(pattern, "grey"):
    print("The word 'grey' got at least one vowel!")
else:
    print("No vowel found!")

if re.search(pattern, "qwertyuiop"):
    print("The word 'qwertyuiop' got at least one vowel!")
else:
    print("No vowel found!")

if re.search(pattern, "rhythm myths"):
    print(" The word 'rhythm myths' got at least one vowel!")
else:
    print("No vowel found!")


### character range matching
print("\ncharacter range matching\n")
### character range matching

pattern2 = r"[A-Z][A-Z][0-9]"

if re.search(pattern2, "NS1 is prefix of first name server address."):
    # Found NS1 as match
    print("OK")
if re.search(pattern2, "You should put a second one with NS2 as prefix."):
    # Found NS2 as match
    print("OK")
if re.search(pattern2, "I don\'t have any nameserver."):
    print("NS3")
else:
    print("Not OK!")
if re.search(pattern2, "PY3"):
    # Found PY3 as match
    print("OK")
