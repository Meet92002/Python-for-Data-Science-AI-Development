# Introduction to Classes and Objects
# Creating a class
# Instances of a Class: Objects and Attributes
# Methods
# Creating a class
# Creating an instance of a class Circle
# The Rectangle Class

# Creating a Class////////////////////

# Import the library

from typing import Dict

import matplotlib.pyplot as plt
# %matplotlib inline # This line is used in Jupyter notebooks to display plots inline

# Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        #gca stands for "get current axis",fc stands for "fill color"
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  


# Creating an instance of a class Circle////////////////////////////////////

# Create an object RedCircle

RedCircle = Circle(10, 'red') 

# Find out the methods can be used on the object RedCircle

dir(RedCircle)

# Print the object attribute radius

RedCircle.radius # output: 10

# Print the object attribute color

RedCircle.color # output: 'red'

# Set the object attribute radius

RedCircle.radius = 1
RedCircle.radius # output: 1

# Call the method drawCircle

RedCircle.drawCircle() # output: A red circle with radius 1 is drawn

# Use method to change the object attribute radius

print('Radius of object:',RedCircle.radius) # output: 1
RedCircle.add_radius(2) # output: 3
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius) 
RedCircle.add_radius(5) # output: 8
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

# Create a blue circle with a given radius

BlueCircle = Circle(radius=100)

# Print the object attribute radius

BlueCircle.radius # output: 100

# Print the object attribute color

BlueCircle.color # output: ERROR

# Call the method drawCircle

BlueCircle.drawCircle() 

# The Rectangle Class/////////////////////////////////////

# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        #output: A rectangle with width 2, height 3 and color red is drawn

# Create a new object rectangle

SkinnyBlueRectangle = Rectangle(2, 3, 'blue')

# Print the object attribute height

SkinnyBlueRectangle.height # output: 3

# Print the object attribute width

SkinnyBlueRectangle.width # output: 2

# Print the object attribute color

SkinnyBlueRectangle.color # output: 'blue'

# Use the drawRectangle method to draw the shape

SkinnyBlueRectangle.drawRectangle() 
#output: A rectangle with width 2, height 3 and color blue is drawn

#Exercise://///////////////////////////////////////////////////

class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)

# Creating objects of the Vehicle class
vehicle1 = Vehicle(200, 20)
vehicle1.assign_seating_capacity(5)
vehicle1.display_properties()

vehicle2 = Vehicle(180, 25)
vehicle2.assign_seating_capacity(4)
vehicle2.display_properties()

# Output:
# Properties of the Vehicle:
# Color: white
# Maximum Speed: 200
# Mileage: 20
# Seating Capacity: 5
# Properties of the Vehicle:
# Color: white
# Maximum Speed: 180
# Mileage: 25
# Seating Capacity: 4

# Add exercises ////////////////////////////////////////

# 1. Inside the constructor, convert the text argument to lowercase using the lower() method.
# 2.Then, remove punctuation marks (periods, exclamation marks, commas, and question marks) from the text using the replace() method.
# 3. Finally, assign the formatted text to a new attribute called fmtText.
class TextAnalyzer(object):
    
    givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
    text = givenstring
    
    def __init__ (self, text):
        # remove punctuation
        self.fmtText = formattedText
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        formattedText = formattedText.lower()
        self.fmtText = formattedText
        print(self.fmtText)
    #output: lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet

# 1. Inside the constructor, convert the text argument to lowercase using the lower() method.
# 2. Then, remove punctuation marks (periods, exclamation marks, commas, and question marks) from the text using the replace() method.
# 3. Finally, assign the formatted text to a new attribute called fmtText.

class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    #output: {'lorem': 2, 'ipsum': 1, 'dolor': 1, 'diam': 5, 'amet': 3, 
    # 'consetetur': 1, 'magna': 2, 'sed': 1, 'nonumy': 1, 'eirmod': 1, 
    # 'tempor': 1, 'et': 4, 'labore': 1}
    
# In this step, you will implement the freqAll() method with the below parameters:
#  1. Split the fmtText attribute into individual words using the split() method.
#  2.Create an empty dictionary to store the word frequency.
#  3. Iterate over the list of words and update the frequency dictionary accordingly.
#  4. Use count method for counting the occurence.
#  5. Return the frequency dictionary.

class TextAnalyzer(object):
    
    givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
    text = givenstring
    
    def __init__ (self, text):
        # remove punctuation
        self.text = formattedText
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        formattedText = formattedText.lower()
        self.fmtText = formattedText
        print(self.fmtText)
    def freqAll(self):
        splitlist = self.fmtText.split()
        Dirct={ }
        for key in splitlist:
            Dict[key] = splitlist.count(key)
        return Dict
    # Output:
    # lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet
    # {'lorem': 2, 'ipsum': 1, 'dolor': 1, 'diam': 5, 'amet': 3, 
    # 'consetetur': 1, 'magna': 2, 'sed': 1, 'nonumy': 1, 'eirmod': 1, 
    # 'tempor': 1, 'et': 4, 'labore': 1}
    
    
# In step-5, you have to implement the freqOf(word) method that takes a word argument:
#  1. Create a method and pass the word that needs to be found.
#  2. Get the freqAll method to look for count and check if that word is in the list.
#  3. Return the count. If the word is not found, the count returned is 0.

class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        self.text = formattedText
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        formattedText = formattedText.lower()
        self.fmtText = formattedText
        print(self.text)
        
    def freqAll(self):
        splitlist = self.fmtText.split()
        Dirct={ }
        for key in splitlist:
            Dict[key] = splitlist.count[key]
        return Dict
        
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
analyzed = TextAnalyzer(TextAnalyzer.givenstring)
print(analyzed.freqAll())
print("Formatted Text:", analyzed.fmtText)
print("string counts the frequency :", analyzed.freqAll())
print(analyzed.freqOf("lorem"))

    # Output:
    # Formatted Text: lorem ipsum dolor diam amet consetetur lorem magna sed diam nonumy eirmod tempor diam et labore et diam magna et diam amet
    # string counts the frequency : {'lorem': 2, 'ipsum': 1, 'dolor': 1, 'diam': 5, 'amet': 3,
    #                               'consetetur': 1, 'magna': 2, 'sed': 1, 'nonumy': 1, 'eirmod': 1,
    #                               'tempor': 1, 'et': 4, 'labore': 1}
    # 2