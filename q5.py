
#--------------------------------------------------------------------#

# Question 5
# Level 1

# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters

#--------------------------------------------------------------------#


class String():

    def __init__(self, input_string: str = None):
        self.input_string = input_string


    def getString(self):
        self.input_string = input("Enter a string\n")
        return self.input_string

    def printString(self):
         printed_string = self.input_string.upper()
         print(printed_string)
         return printed_string

    
def test(object):
        print("Testing getString method...\n")
        result = object.getString()
        assert result.isalpha() == True
        print("Test successful\n")

        print("Testing printString method...\n")
        resultUpper = str(object.printString())
        assert resultUpper.isupper() == True
        print("Test successful\n")


q5 = String()

test(q5)
q5.getString()
q5.printString()


