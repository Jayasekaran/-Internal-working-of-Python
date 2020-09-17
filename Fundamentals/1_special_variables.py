print("# before import")
import math

print("# before findFactorial")
def findFactorial(x):    
    print("# factorial of ".format(x), "   :", math.factorial(x))

print("# before findSquareRoot")
def findSquareRoot(x):
    print("# square of root".format(x), "   :", math.sqrt(x))

print("# before __name__ guard")
if __name__ == '__main__':
    findFactorial(10)
    findSquareRoot(100)
print("# after __name__ guard")
# Whenever the Python interpreter reads a source file, it does two things:

# 1. it sets a few special variables like __name__, and then
# 2. it executes all of the code found in the file.
# Let's see how this works and how it relates to the __name__ checks

# It's as if the interpreter inserts this at the top
# of your module when run as the main program.
# '__name__ = "__main__" '

# This Module(1_special_variables) Is Imported By Another
# It's as if the interpreter inserts this at the top
# of your module when it's imported from another module.
# '__name__ = "__1_special_variables__" '