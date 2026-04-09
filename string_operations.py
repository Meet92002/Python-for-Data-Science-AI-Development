# What are Strings?
# Indexing
# Negative Indexing
# Slicing
# Stride
# Concatenate Strings
# Escape Sequences
# String Manipulation Operations

# Use quotation marks for defining string

"The BodyGuard"

# Use single quotation marks for defining string

'The BodyGuard'

# Digitals and spaces in string

'1 2 3 4 5 6 '

# Special characters in string

'@#2_#]&*^%$'

# Print the string

print("hello!")

# Assign string to variable

name = "The BodyGuard"
name

# Indexing/////////


Name = "The BodyGuard"

# Print the first element in the string

print(name[0])

# Print the element on index 6 in the string

print(name[6])

# Print the element on the 10th index in the string

print(name[10])


# Negative Indexing///////////////

Name = "The BodyGuard"

# Print the last element in the string
print(name[-1])
 
# Print the element on index -6 in the string
print(name[-6])

# Print the element on index -10 in the string
print(name[-10])

# Slicing///////////////////

Name = "The BodyGuard"

# Print the first three characters in the string
print(Name[0:3])

# Print the characters from index 4 to index 7 in the string
print(Name[4:8])

# Print the characters from index 8 to the end of the string
print(Name[8:])


# Stride/////////////////////////
Name = "The BodyGuard"

# Get every second element, starting with the index 0. The elments on index 0, 2, 4 ...

name[::2]

# Get every second element in the range from index 0 to index 4

name[0:5:2]

# Concatenate two Strings//////////////////////

first_name = "The"
last_name = "BodyGuard"

# Concatenate first_name and last_name with a space in between
full_name = first_name + " " + last_name
full_name   

# Escape Sequences//////////////////////////

# New line escape sequence

print(" The BodyGuard\n is the best album" )

# Tab escape sequence

print(" The BodyGuard \t is the best album" )

# Include back slash in string

print(" The BodyGuard \\ is the best album" )

# r will tell python that string will be display as raw string

print(r" The BodyGuard \ is the best album" )


# String Manipulation Operations//////////////////////////

# Convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)
# output - before upper: Thriller is the sixth studio album
# output - After upper: THRILLER IS THE SIXTH STUDIO ALBUM


## Replace the old substring with the new target substring is the segment has been found in the string
a = "The BodyGuard is the best album"
b = a.replace('BodyGuard', 'Janet')
b # output - 'The Janet is the best album'

# Find the substring in the string. Only the index of the first elment of substring in string will be the output
name = "The BodyGuard"
name.find('he') # output - 1

# Find the substring in the string.
name.find('Guard') # output - 8

# If cannot find the substring in the string
name.find('Jasdfasdasdf') # output - -1

#Split the substring into list
name = "The BodyGuard"
split_string = (name.split())
split_string # output - ['The', 'BodyGuard']

# RegEx//////////////////////////////

import re

s1 = "The BodyGuard is the best album"

# Define the pattern to search for
pattern = r"Body"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")   # output - Match found!

# \d	Matches any digit character (0-9)	"123" matches "\d\d\d"
# \D	Matches any non-digit character	"hello" matches "\D\D\D\D\D"
# \w	Matches any word character (a-z, A-Z, 0-9, and _)	"hello_world" matches "\w\w\w\w\w\w\w\w\w\w\w"
# \W	Matches any non-word character	"@#$%" matches "\W\W\W\W"
# \s	Matches any whitespace character (space, tab, newline, etc.)	"hello world" matches "\w\w\w\w\w\s\w\w\w\w\w"
# \S	Matches any non-whitespace character	"hello_world" matches "\S\S\S\S\S\S\S\S\S\S\S"
# \b	Matches the boundary between a word character and a non-word character	"cat" matches "\bcat\b" in "The cat sat on the mat"
# \B	Matches any position that is not a word boundary	"cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"


pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match") # output - Phone number found: 1234567890

# ///////////////////////////

pattern = r"\W "  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches) # output - Matches: [',', ' ', '!']

#////////////////////////////
s2 = "The BodyGuard is the best album of 'Whitney Houston'."

# Use the findall() function to find all occurrences of the "st" in the string

result = re.findall("st", s2)

# Print out the list of matched words
print(result) # output - ['st', 'st']

# ///////////////////////////////////

s2 = "The BodyGuard is the best album of 'Whitney Houston'."
# Use the split function to split the string by the "\s"
split_array = re.split(r"\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array)
#output - ['The', 'BodyGuard', 'is', 'the', 'best', 'album', 'of', "'Whitney", "Houston'."]

#/////////////////////////////////
 
# Define the regular expression pattern to search for
s2 = "The BodyGuard is the best album of 'Whitney Houston'."
pattern = r"Whitney Houston"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE) # re.IGNORECASE makes the search case-insensitive, so it matches "Whitney Houston" in any letter case

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 

# output - The BodyGuard is the best album of 'legend'.