# Functions
# What is a function?
# Variables
# Functions Make Things Simple
# Pre-defined functions
# Using if/else Statements and Loops in Functions
# Setting default argument values in your custom functions
# Global variables
# Scope of a Variable
# Collections and Functions
# Quiz on Loops

# Functions :- 
#   A function is a block of code that performs a specific task. It can take inputs,
#   process them, and return an output. Functions help to break down complex problems into 
#   smaller, manageable pieces, making code more organized and reusable.

# What is a function?
# You can define functions to provide the required functionality. Here are simple rules to define a function in Python:

# Functions blocks begin def followed by the function name and parentheses ().
# There are input parameters or arguments that should be placed within these parentheses.
# You can also define parameters inside these parentheses.
# There is a body within every function that starts with a colon (:) and is indented.
# You can also place documentation before the body.
# The statement return exits a function, optionally passing back a value.

# First function example: Add 1 to a and store as b

def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b) 
add(1) # Output: 1 if you add one 2

# Get a help on add function

help(add) 

# Call the function add()

add(1)

# Call the function add()

add(2)

# Define a function for multiple two numbers

def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result) # Output: 24

# Use mult() multiply two integers

Mult(2, 3) # Output: 6

# Use mult() multiply two floats

Mult(10.0, 3.14) # Output: 31.400000000000002

# Use mult() multiply two different type values together

Mult(2, "The BodyGuard ") # Output: 'The BodyGuard The BodyGuard '(string is repeated 2 times)

# Variables////////////////////

# Function Definition

def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)
# Directly enter a number as parameter 
square(2) # Output: 2 if you square + 1 5

# Initializes Global variable  

x = 3
# Makes function call and return function a y
y = square(x)
y # Output: 3 if you square + 1 10

# Define functions, one with return value None and other without return value
# Printing the function after a call reveals a None is the default return statement:
def MJ():
    print('The BodyGuard')
    
def MJ1():
    print('The BodyGuard')
    return(None)
MJ() # Output: The BodyGuard
MJ1() # Output: The BodyGuard

# See what functions returns are

print(MJ()) # Output: The BodyGuard
print(MJ1()) # Output: The BodyGuard

# Define the function for combining strings

def con(a, b):
    return(a + b)
# Test on the con() function

con("This ", "is") # Output: 'This is'

# Functions Make Things Simple ///////////////////////////////////

# Block 1:

# a and b calculation block1

a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5
c1   # Output: 5
# Block 2:

# a and b calculation block2

a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5
c2  # Output: 0

# Make a Function for the calculation above

def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
        print(c)
    else:
        c = 5
    return(c) 

a2 = 0
b2 = 0
c1 = Equation(a2, b2)
#output: 0

#Block 3:

a1 = 4
b1 = 5
c1 = Equation(a1, b1)
c1 # Output: 5

#Block 4:
a2 = 0
b2 = 0
c2 = Equation(a2, b2)
c2 # Output: 0

# Pre-defined functions /////////////////////////////////////

# Build-in function print()

album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings) # Output: [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]

# Use sum() to add every element in a list or tuple together

sum(album_ratings) # Output: 70.5

# Show the length of the list or tuple

len(album_ratings) # Output: 8

# In-Built functions ///////////////////////////////////////

#You will see below will return an error as integer alone is not considered while using a function.
#It either has to be in the form of tuple, list or a set.

sum(1,2) # Output: TypeError: sum() takes at most 2 arguments (3 given)

# Define a tuple
a = (1, 2)

# Pass the tuple to the sum function and store the result in a variable
c = sum(a)

# Print the result
print(f"The sum of the elements in the tuple {a} is {c}.")
# Output: The sum of the elements in the tuple (1, 2) is 3.

# Define a list
a = [1, 2]

# Pass the list to the sum function and store the result in a variable
c = sum(a)

# Print the result
print(f"The sum of the elements in the list {a} is {c}.")
# Output: The sum of the elements in the list [1, 2] is 3.

# Using if/else Statements and Loops in Functions /////////////////////////////////////

# Function example

def type_of_album(album, year_released):
    
    print(album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("The BodyGuard", 1980)
print(x) 
# Output: The BodyGuard 1980
          # Oldie   

# We can use a loop in a function. For example, we can print out each element in a list:
# Print the list using for loop


def PrintList(the_list):
    for element in the_list:
        print(element)
PrintList(['1', 1, 'the man', "abc"])
# Output: 1
#         1
#         the man
#         abc

# String comparison in Functions

#Compare Two Strings Directly using in operator
# add string
string= "The BodyGuard is the best album"

# Define a funtion
def check_string(text):
    
# Use if else statement and 'in' operatore to compare the string
    if text in string:
        return 'String matched'
    else:
        return 'String not matched'

check_string("The BodyGuard is the best")
# Output: String matched

#Compare two strings using == operator and function
def compareStrings(x, y):
# Use if else statement to compare x and y
    if x==y:
        return 1
    
# Declare two different variables as string1 and string2 and pass string in it
string1 = "The BodyGuard is the best album"
string2 = "The BodyGuard is the best album"

# Declare a variable to store result after comparing both the strings
check = compareStrings(string1, string2)

#Use if else statement to compare the string
if check==1:
    print("\nString Matched")
else:
    print("\nString not Matched")

# Output: String Matched


# Python Program to Count words in a String using Dictionary
def freq(string):
    
    #step1: A list variable is declared and initialized to an empty list.
    words = []
    
    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()
    
    #step3: Declare a dictionary
    Dict = {}
    
    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
    
    #step5: Print the dictionary  
    print("The Frequency of words is:",Dict)
    
#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")

#out put: The Frequency of words is: 
# {'Mary': 4, 'had': 3, 'a': 3, 'little': 5, 'lamb': 5, 'Little': 1, 'lamb,': 1, 'lamb.': 1, 'Its': 1, 
# 'fleece': 1, 'was': 2, 'white': 1, 'as': 1, 'snow': 1, 'And': 1, 'everywhere': 2, 'that': 2, 
# 'went': 3, 'went,': 1, 'Everywhere': 1, 'The': 1, 'sure': 1, 'to': 1, 'go': 1}


# Setting default argument values in your custom functions

# Example for setting param with default value

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

isGoodRating() # Output: this album sucks it's rating is 4
isGoodRating(10) # Output: this album is good its rating is 10

# Global variables ///////////////////////////////////////////

album = "The BodyGuard"
def printer1(album):
    internal_var1 = "Thriller"
    print(album, "is an album")
    
printer1(album) # Output: The BodyGuard is an album

# local variable and global variable
album = "The BodyGuard"
def printer(album):
    global internal_var 
    internal_var= "Thriller"
    print(album,"is an album")

printer(album) # Output: The BodyGuard is an album
printer(internal_var) # Output: Thriller

# Scope of a Variable ///////////////////////////////////////////

# Example of global variable

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC")) 
# Output: AC/DC's rating is: 10.0
print("Deep Purple's rating is:",getBandRating("Deep Purple")) 
# Output: Deep Purple's rating is: 0.0
print("My favourite band is:", myFavouriteBand)
# Output: My favourite band is: AC/DC

# Deleting the variable "myFavouriteBand" from the previous example to demonstrate an example of a local variable 

del myFavouriteBand

# Example of local variable

def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
# Output: AC/DC's rating is:  10.0
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
# Output: Deep Purple's rating is:  0.0
print("My favourite band is", myFavouriteBand)
# Output: NameError: name 'myFavouriteBand' is not defined

# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
# Output: AC/DC's rating is: 0.0
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
# Output: Deep Purple's rating is:  10.0
print("My favourite band is:",myFavouriteBand)
# Output: My favourite band is: AC/DC

# Collections and Functions ///////////////////////////////////////////

# All the arguments are 'packed' into args which can be treated like a tuple
def printAll(*args): 
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')
# Output: No of arguments: 3
#         Horsefeather
#         Adonis
#         Bone
#         No of arguments: 4
#         Sidecar
#         Long Island
#         Mudslide
#         Carriage

# Similarly, The arguments can also be packed into a dictionary as shown:

def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])
    
printDictionary(Country='Canada',Province='Ontario',City='Toronto')
# Output: Country : Canada
#         Province : Ontario
#         City : Toronto

def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

myList # Output: ['One', 'Two', 'Three', 'Four']