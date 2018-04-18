
# Recursive function:

print("\nprint from 1 to 4")
def recursive(n):
    if n==0:
        return n
    recursive(n-1)
    print(n)

print(recursive(4))

print("\nprint 4 to 1")
def recursive(n):
    if n==0:
        return n
    print(n)
    recursive(n-1)

print(recursive(4))

print("\nprint from 1 to 4 and 4 to 1")
def recursive(n):
    if n==0:
        return n
    print(n)
    recursive(n-1)
    print(n)

print(recursive(4))

