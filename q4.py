# Question 4
# Level 1

# Question:
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple


print("My Solution")
input_list = input('Enter numbers separated by space\n')
list = input_list.split()
print(list)

tuplet = tuple(list)
print(tuplet)

# Difference between a list and a tuple:
#   - List is ordered and changeable; a tuple is ordered and unchangeable
#   - List has []; tuple has ()
#   - In a dictionary, we CANNOT use lists as key; In a dicitonary, we can create keys using tuples

print("Their Solution")
values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)