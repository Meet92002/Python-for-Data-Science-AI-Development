# About the Dataset
# Lists
# Indexing
# List Content
# List Operations
# Copy and Clone List
# Quiz on Lists
# Scenario:Shopping List


# The table has one row for each movie and several columns:

# Artist - Name of the artist
# Album - Name of the album
# Released_year - Year the album was released
# Length_min_sec - Length of the album (hours,minutes,seconds)
# Genre - Genre of the album
# Music_recording_sales_millions - Music recording sales (millions in USD) on SONG://DATABASE
# Claimed_sales_millions - Album's claimed sales (millions in USD) on SONG://DATABASE
# Released - Date on which the album was released
# Soundtrack - Indicates if the album is the movie soundtrack (Y) or (N)
# Rating_of_friends - Indicates the rating from your friends from 1 to 10

# Create a list

L = ["The Bodyguard", 7.0, 1992]
L #output - ['The Bodyguard', 7.0, 1992]

# Print the elements on each index

print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )

#output - the same element using negative and positive indexing:
        #  Postive: The Bodyguard 
        #  Negative: The Bodyguard
        # the same element using negative and positive indexing:
        #  Postive: 7.0 
        #  Negative: 7.0
        # the same element using negative and positive indexing:
        #  Postive: 1992 
        #  Negative: 1992

# List Content///////////////////////////

# Sample List

L = ["The Bodyguard", 7.0,1992,"BG",1]
L # output - ['The Bodyguard', 7.0, 1992, 'BG', 1]

# List slicing

L[3:5] # output - ['BG', 1]

# Use extend to add elements to list

L = [ "The Bodyguard", 7.0]
L.extend(['pop', 10])
L # out put - ['The Bodyguard', 7.0, 'pop', 10]

# Use append to add elements to list

L = [ "The Bodyguard", 7.0]
L.append(['pop', 10])
L # out put - ['The Bodyguard', 7.0, ['pop', 10]]

# Use extend to add elements to list

L = [ "The Bodyguard", 7.0]
L.extend(['pop', 10])
L # out put - ['The Bodyguard', 7.0, 'pop', 10]

# Use append to add elements to list

L.append(['a','b'])
L # out put - ['The Bodyguard', 7.0, 'pop', 10, ['a', 'b']]

# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)
# out put - Before change: ['disco', 10, 1.2], After change: ['hard rock', 10, 1.2]

# Delete the element based on the index

print('Before change:', A)
del(A[0])
print('After change:', A) 
# out put - Before change: ['hard rock', 10, 1.2], After change: [10, 1.2]

# Split the string, default is by space

'hard rock'.split() # output - ['hard', 'rock']

# Split the string by comma

'A,B,C,D'.split(',') # output - ['A', 'B', 'C', 'D']


# Copy and Clone List///////////////////////////////

# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B) # out put - A: ['hard rock', 10, 1.2] B: ['hard rock', 10, 1.2]

# Examine the copy by reference
A = ["hard rock", 10, 1.2]
B = A
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0]) # out put - B[0]: hard rock B[0]: banana

# Clone (clone by value) the list A
A = ["hard rock", 10, 1.2]
B = A
print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])
B = A[:]
B # out put - B[0]: hard rock B[0]: banana

# Now if you change A, B will not change:
A = ["hard rock", 10, 1.2]
B = A
A[0] = "banana"
print('B[0]:', B[0])
B = A[:]
A[0] = "hard rock"
print('A[0]:', A[0])
print('B[0]:', B[0]) # out put - B[0]: banana A[0]: hard rock B[0]: banana