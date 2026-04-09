# Condition Statements
# Comparison Operators
# Branching
# Logical operators

# Condition Statements ///////////////////////////////////

# Comparison Operators
#       equal: ==
#       not equal: !=
#       greater than: >
#       less than: <
#       greater than or equal to: >=
#       less than or equal to: <=

# Condition Equal

a = 5
a == 6 # output - False

# Greater than Sign

i = 6
i > 5 # output - True

# Greater than Sign

i = 2
i > 5 # output - False

# Inequality Sign

i = 2
i != 6 # output - True

# Inequality Sign

i = 6
i != 6 # output - False

# Use Equality sign to compare the strings

"ACDC" == "The Bodyguard" # output - False

# Use Inequality sign to compare the strings

"ACDC" != "The Bodyguard" # output - True

# Compare characters
    
'B' > 'A'   # output - True

# Compare characters

'BA' > 'AB'   # output - True


# Branching //////////////////////////////////// 

# If statement example

age = 19
#age = 18

#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")
#output - you can enter
#         move on


# Else statement example

age = 18
# age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")
#output - go see Meat Loaf
#         move on           


# Elif statment example

age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")
#output - go see Pink Floyd
#         move on


# Condition statement example

# album_year = 1983
album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
    
print('do something..')
#output - do something..


# Condition statement example

album_year = 1983
#album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')
#output - Album year is greater than 1980
#         do something..    


# Logical operators (and, or, not) ////////////////////////////////////

# Condition statement example

album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("Do Stuff..")
#output - Album year was in between 1980 and 1989
#         Do Stuff..    


# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 90's")
else:
    print("The Album was made in the 1980's ")
#output - Album was not made in the 90's  


# Condition statement example

album_year = 1983

if not (album_year == 1984):
    print ("Album year is not 1984")
#output - Album year is not 1984
