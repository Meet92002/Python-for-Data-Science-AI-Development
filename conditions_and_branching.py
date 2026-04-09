# Condition Statements
# Comparison Operators
# Branching
# Logical operators
# Quiz on Conditions

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

# Quiz on Conditions//////////////////////////////////////////

""" Player Name	Sport	Achievements
Serena Williams	Tennis	23 Grand Slams
Lionel Messi	Soccer	7 Ballon d'Ors
Michael Phelps	Swimming	23 Gold Medals
Usain Bolt	Athletics	8 Gold Medals
Roger Federer	Tennis	20 Grand Slams
Cristiano Ronaldo	Soccer	5 Ballon d'Ors """



# Write your code below and press Shift+Enter to execute
player_name = "Lionel Messi"
sport = "Soccer"
achievements = 11
if achievements > 10:
    print("Lionel Messi, Soccer, and 7 Ballon d'Ors")
    print(f"{player_name} plays {sport} and has {achievements} achievements.")
else:
    print("does not have more than 10 achievements.")
#output - Lionel Messi, Soccer, and 7 Ballon d'Ors
#         Lionel Messi plays Soccer and has 11 achievements.

# Write your code below and press Shift+Enter to execute
user_name = "Roger Federer"
sports = "Tennis"
achievements = 20

if sports == 'Tennis' or achievements == 20:
    print("Achieved successful")
#output - Achieved successful


# Write your code below and press Shift+Enter to execute
user_name = "Usain Bolt"
sports = "Athletics"
achievements = 8

if achievements < 10 and sports != "soccer":
    print(f" The player name is {user_name}, he played {sports} sport game and his achievements was {achievements} gold medals")
else:
    print(" That data not match with their criteria")

#output -  The player name is Usain Bolt, 
#           he played Athletics sport game and his achievements was 8 gold medals
