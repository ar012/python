## Find out factorials of every numbers from 1 to 10.
fact = 1
for i in range(1, 11):
    fact *= i
    print("Factorial of", i, "is", fact)
    i = i+1