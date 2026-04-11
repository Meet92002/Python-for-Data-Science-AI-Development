# What is an Exception?
# Exception Handling

# Definition

# An exception is an error that occurs during the execution of code. This error causes the code to raise an exception and if not prepared to handle it will halt the execution of the code.

# Examples

from matplotlib.pylab import number


1/0 #output: ZeroDivisionError: division by zero
a = ""
y = a + 5 #output: NameError: name 'a' is not defined

a = [1, 2, 3]
a[10] #output: IndexError: list index out of range


# Try Except Example //////////////////

a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")
# Output:
# Please enter a number to divide a: 0
# There was an error
#       OR
# Please enter a number to divide a 4
# Success a= 0.25

# Try Except Specific example //////////////////

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided can't divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
# Output:
# Please enter a number to divide a: 0 
# The number you provided can't divide 1 because it is 0
#       OR
# Please enter a number to divide a: hello
# You did not provide a number 
#       OR
# Please enter a number to divide a: 4  
# Success a= 0.25

# Try Except Else and else OR Finally ///////////////////   

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
# Output:
# Please enter a number to divide a: 0  
# The number you provided cant divide 1 because it is 0
#       OR
# Please enter a number to divide a: hello
# You did not provide a number
#       OR
# Please enter a number to divide a: 4
# success a= 0.25

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")
# Output:
# Please enter a number to divide a: 0
# The number you provided cant divide 1 because it is 0
# Processing Complete
#       OR
# Please enter a number to divide a: hello
# You did not provide a number
# Processing Complete
#       OR
# Please enter a number to divide a: 4
# success a= 0.25
# Processing Complete

# Exercise ////////////////////////////

import math

def perform_calculation(number1):
    try:
        result = math.sqrt(number1)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input! Please enter a positive integer or a float value.")
# Test case
number1=float(input("Enter the number:-"))
perform_calculation(number1)

# Output:
# Enter the number:- 4
# Result: 2.0
#       OR
# Enter the number:- 9
# Result: 3.0
#       OR
# Enter the number:- -2
# Error: Invalid input! Please enter a positive integer or a float value.

def complex_calculation(num):
    try:
        result = num / (num - 5)
        print (f"Result: {result}")
    except Exception as e:
        print("An error occurred during calculation.")
# Test case
user_input = float(input("Enter a number: "))
complex_calculation(user_input)
# Output:
# Enter a number: 10
# Result: 2.0
#       OR
# Enter a number: 5
# An error occurred during calculation.

