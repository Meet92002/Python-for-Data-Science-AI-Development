# Introduction to Classes and Objects
# Creating a class
# Instances of a Class: Objects and Attributes
# Methods
# Creating a class
# Creating an instance of a class Circle
# The Rectangle Class

# Creating a Class////////////////////

# Import the library

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