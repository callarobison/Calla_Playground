# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


# My Solution


n= int(input("Give me a number"))
fact = n

for x in range (1, n-1):
    fact = fact*(n-x)
    print(fact)

# Their Solution
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(raw_input())
print(fact(x))










