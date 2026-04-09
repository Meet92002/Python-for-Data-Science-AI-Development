# About the Dataset
# Tuples
# Indexing
# Slicing
# Sorting


'''
The table has one row for each movie and several columns:

Artist - Name of the artist
Album - Name of the album
Released_year - Year the album was released
Length_min_sec - Length of the album (hours,minutes,seconds)
Genre - Genre of the album
Music_recording_sales_millions - Music recording sales (millions in USD) on SONG://DATABASE
Claimed_sales_millions - Album's claimed sales (millions in USD) on SONG://DATABASE
Date_released - Date on which the album was released
Soundtrack - Indicates if the album is the movie soundtrack (Y) or (N)
Rating_of_friends - Indicates the rating from your friends from 1 to 10 '''

# Tuples ////////////////////////////

# Create your first tuple

tuple1 = ("disco",10,1.2 )
tuple1 # output - ('disco', 10, 1.2)

# Print the type of the tuple you created

type(tuple1) # output - <class 'tuple'>

# Indexing ///////////////////////////

# Print the variable on each index

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
#output - disco
#         10
#         1.2

# Print the type of value on each index

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))
# output - disco <class 'str'>
#          10    <class 'int'>
#          1.2   <class 'float'>

# Use negative index to get the value of the last element

tuple1[-1] # output - 1.2

# Use negative index to get the value of the second last element

tuple1[-2] # output - 10

# Use negative index to get the value of the third last element

tuple1[-3] # output - 'disco'

# Concatenate Tuples ///////////////////////////

tuple2 = tuple1 + ("hard rock", 10)
tuple2 # output - ('disco', 10, 1.2, 'hard rock', 10)

# Slicing ///////////////////////////

# Slice from index 0 to index 2

tuple2[0:3] # output - ('disco', 10, 1.2)

# Slice from index 3 to index 4

tuple2[3:5] # output - ('hard rock', 10)

# Get the length of tuple

len(tuple2) # output - 5

# Sorting /////////////////////////////

# A sample tuple

Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2) # output - (0, 9, 6, 5, 10, 8, 9, 6, 2)

# Sort the tuple

RatingsSorted = sorted(Ratings)
RatingsSorted # output - [0, 2, 5, 6, 6, 8, 9, 9, 10]

# Nested Tuples ///////////////////////////

# Create a nest tuple

NestedT =(1, 2, ("pop", "rock"),(3,4),("disco",(1,2)))

# Print element on each index

print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])
# output - Element 0 of Tuple:  1
#          Element 1 of Tuple:  2    
#          Element 2 of Tuple:  ('pop', 'rock')
#          Element 3 of Tuple:  (3, 4)
#          Element 4 of Tuple:  ('disco', (1, 2))


# Print element on each index, including nest indexes

print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])
#output - Element 2, 0 of Tuple:  pop
#         Element 2, 1 of Tuple:  rock
#         Element 3, 0 of Tuple:  3
#         Element 3, 1 of Tuple:  4
#         Element 4, 0 of Tuple:  disco
#         Element 4, 1 of Tuple:  (1, 2)


# Print the first character of the second element in the first nested tuple

NestedT[2][1][0] # output - 'r'

# Print the second character of the second element in the first nested tuple

NestedT[2][1][1] # output - 'o'

# Print the first element of the nested tuple inside the fifth element of the main tuple.

NestedT[4][1][0] # output - 1

# Print the second element of the nested tuple inside the fifth element of the main tuple.

NestedT[4][1][1] # output - 2


