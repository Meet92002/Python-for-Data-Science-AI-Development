# Types of objects in Python

# Integers
# Floats
# Converting from one object type to a different object type
# Boolean data type
# Exercise: Types


# Integer

11

# Float

2.14

# String

"Hello, Python 101!"

# Type of 12

type(12) # output - int

# Type of 2.14

type(2.14) # output - float

# Type of "Hello, Python 101!"

type("Hello, Python 101!") # output - String

########### Converting from one object type to a different object type ############

# Convert 2 to a float

float(2) # output - 2.0

# Convert integer 2 to a float and check its type

type(float(2)) # output - float 2.0

# Casting 1.1 to integer will result in loss of information

int(1.1) # output - 1

# Convert a string into an integer

int('1') # output - 1

# Convert a string into an integer with error

int('1 or 2 people') # output - error


# Convert the string "1.2" into a float

float('1.2') # output - 1.2

# Convert an integer to a string

str(1) # output - '1'

# Convert a float to a string

str(1.2) # output - '1.2'

# Convert True to int

int(True) # output - 1

# Convert 1 to boolean

bool(1) # output - True

# Convert 0 to boolean

bool(0) # output - False