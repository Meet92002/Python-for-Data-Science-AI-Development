# Sets
# Set Content
# Set Operations
# Sets Logic Operations

#Sets //////////////////////////////////////
# Create a set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1   # output - {'rock', 'R&B', 'soul', 'disco', 'hard rock', 'pop'}

# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set 
# output - {'00:42:19', 10.0, 1982,'30-Nov-82', 46.0, 65,'Michael Jackson', None, 
#           'Pop, Rock, R&B','Thriller'}

# Convert list to set

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
music_genres 
#output - {'rock', 'R&B', 'soul', 'disco', 'hard rock', 'progressive rock',
#          'soft rock', 'pop', 'folk rock'} 

# Set Operations ////////////////////////////////////

# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])
A  # output - {'AC/DC', 'Thriller', 'Back in Black'}

# Add element to set

A.add("NSYNC")
A # output - {'AC/DC', 'Thriller', 'Back in Black', 'NSYNC'}

# Try to add duplicate element to the set

A.add("NSYNC")
A # output - {'AC/DC', 'Thriller', 'Back in Black', 'NSYNC'}

# Remove the element from set

A.remove("NSYNC")
A # output - {'AC/DC', 'Thriller', 'Back in Black'}

# Verify if the element is in the set

"AC/DC" in A # output - True

# Sets Logic Operations////////////////////////////////////

# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets

album_set1, album_set2
# output - ({'AC/DC', 'Thriller', 'Back in Black'},
#           {'AC/DC', 'Back in Black', 'The Dark Side of the Moon'})

# Find the intersections

intersection = album_set1 & album_set2
intersection # output - {'AC/DC', 'Back in Black'}

# Find the difference in set1 but not set2

album_set1.difference(album_set2)  # output - {'Thriller'}

album_set2.difference(album_set1)  # output - {'The Dark Side of the Moon'}

# Use intersection method to find the intersection of album_list1 and album_list2

album_set1.intersection(album_set2)   # output - {'AC/DC', 'Back in Black'}

# Find the union of two sets

album_set1.union(album_set2) # output - {'AC/DC', 'Thriller', 'Back in Black', 
#                                        'The Dark Side of the Moon'}

# Check if superset 
# in this case, we are checking if album_set1 all elements are equal to album_set2, then it is a superset of album_set2
set(album_set1).issuperset(album_set2)  # output - False

# Check if subset
album_set1.issubset(album_set1)  # output - True
print("album_set1 is subset of album_set1:", album_set1.issubset(album_set1))

# Check if subset

set(["Back in Black", "AC/DC"]).issubset(album_set1) # output - True

# Check if superset

album_set1.issuperset({"Back in Black", "AC/DC"})   # output - True