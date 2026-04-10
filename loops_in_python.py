# Loops
# Range
# What is for loop?
# What is while loop?
# Quiz on Loops

# Loops ///////////////////////////////////////////

# Range
# Use the range

range(3) # output - range(0, 3)

# For loop example //////////////////////////////////

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i]) 
# output - 1982
#          1980
#          1973

# Example of for loop

for i in range(0, 8):
    print(i)
# output - 0
#          1
#          2
#          3
#          4
#          5
#          6
#          7

# Exmaple of for loop, loop through list

for year in dates:  
    print(year)   
# output - 1982
#          1980
#          1973 

# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])
# Before square  0 is red
# After square  0 is white
# Before square  1 is yellow
# After square  1 is white
# Before square  2 is green
# After square  2 is white
# Before square  3 is purple
# After square  3 is white
# Before square  4 is blue
# After square  4 is white

# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)
# output - 0 red
#          1 yellow 
#          2 green
#          3 purple
#          4 blue

# while loop //////////////////////////////////////

# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")
#output - 1982
#         1980
#         It took  2 repetitions to get out of loop.    


# Controlling Loop Execution with break and continue //////////////////////////////////////

# The break statement
for num in range(1, 10):
    if num == 5:
        print("Breaking the loop at:", num)
        break
    print(num)
# output - 1
#          2
#          3
#          4
# Breaking the loop at: 5


# The continue statement
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
# output - 1
#          2
#          4
#          5


# Using break and continue in a while loop
count = 0
while count < 10:
    count += 1
    if count == 3:
        continue  # skip printing 3
    if count == 8:
        break     # stop the loop when count is 8
    print(count)
# output - 1
#          2    
#          4
#          5
#          6
#          7

# Quiz on Loops//////////////////////////////////////////

# 1.Write a for loop that prints out all the elements between -5 and 5 using the range function.
for i in range(-5, 6):
    print(i, end=',')
# output - -5,-4,-3,-2,-1,0,1,2,3,4,5,

# 2. Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']. Make sure you follow Python conventions.
genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for gener in range(len(genres)):
    print(genres[gener])
# output - rock
#          R&B
#          Soundtrack
#          R&B
#          soul
#          pop

# 3. Write a for loop that prints out the following list: squares=['red', 'yellow', 'green', 'purple', 'blue']

squares=['red', 'yellow', 'green', 'purple', 'blue']
for i in squares:
    print(i)
# output - red
#          yellow   
#          green
#          purple
#          blue     

# 4. Write a while loop to display the values of the Rating of an album playlist stored in thePlayListRatings list. If the score is less than 6, exit the loop. The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

# PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
# i =0
# while (i < len(PlayListRatings)):
#     if PlayListRatings[i] < 6:
#         break
#     print(PlayListRatings[i])
#     i += 1
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
Rating = PlayListRatings[0]
while(i < len(PlayListRatings) and Rating >= 6):
    print(Rating)
    i = i + 1 # This prints the value 10 only once 
    Rating = PlayListRatings[i]
    i = i + 1
# output - 10
#          9.5
#          10
#          8
#          7.5


#5. Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while (i< len(squares) and squares[i] == "orange"):
    new_squares.append(squares[i])
    i += 1
print(new_squares)

    # if you want all string of orange

# squares = ['orange', 'orange', 'purple', 'blue', 'orange']
# new_squares = []

# i = 0

# while i < len(squares):
#     if squares[i] == 'orange':
#         new_squares.append(squares[i])
#     i += 1

# print(new_squares)

# output - ['orange', 'orange']

#6. Write a Python program using a for loop that prints numbers from 1 to 15 but:

# Skips multiples of 3
# Stops the loop if the number is greater than 12

for i in range(1, 16):
    if i % 3 == 0:
        continue  # skip multiples of 3
    if i > 12:
        break     # stop if number > 12
    print(i)

# output - 1
#          2
#          4
#          5
#          7
#          8
#          10
#          11
