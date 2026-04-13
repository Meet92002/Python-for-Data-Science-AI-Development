# What is Numpy?
# Type
# Assign Value
# Slicing
# Assign Value with List
# Other Attributes
# Numpy Array Operations
# Array Addition
# Array Multiplication
# Product of Two Numpy Arrays
# Dot Product
# Adding Constant to a Numpy Array
# Mathematical Functions
# Linspace

# import numpy library

import numpy as np

a = np.array([0, 1, 2, 3, 4])
a
# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# Checking NumPy Version
print(np.__version__)

# Check the type of the array

type(a)

# Check the type of the values stored in numpy array

a.dtype

# Example

import numpy as np
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
type(b) # output: numpy.ndarray
b.dtype # output: dtype('float64')

# Assign value

# Create numpy array

c = np.array([20, 1, 2, 3, 4])
c[0] = 100
c[4] = 0

#output: [100,1,2,3,0]

# Slicing///////////////


# Slicing the numpy array
c = np.array([20, 1, 2, 3, 4])
d = c[1:4] # output: [1, 2, 3]
c[3:5] = 300, 400 # output : array([ 10,   2,  30, 300, 400])


# We can also define the steps in slicing, like this: [start:end:step].
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2]) #output: [2 4]
print(arr[:4]) # output: [1, 2, 3, 4]
print(arr[4:]) # output: [5, 6, 7]
print(arr[1:5:]) # output: [2, 3, 4, 5]
print(arr[1: :2]) #output: [2, 4, 6]

# Other Attributes ////////////////////////////

# Get the size of numpy array
arr.size #output: 7

# Get the number of dimensions of numpy array
a.ndim #output: 1

# Get the shape/size of numpy array
a.shape #output: (7, )

# Numpy Statistical Functions ///////////////////////////

# Create a numpy array

a = np.array([1, -1, 1, -1])

# Get the mean of numpy array

mean = a.mean()
mean #output: 0.0

# Get the standard deviation of numpy array

standard_deviation=a.std()
standard_deviation #output: 1.0

# Create a numpy array

b = np.array([-1, 2, 3, 4, 5])
b

# Get the biggest value in the numpy array

max_b = b.max()
max_b #output:5

# Get the smallest value in the numpy array

min_b = b.min()
min_b #output: -1

# Numpy Array Operations/////////////////////////////////

# Array Addition, Subtraction, Multiplication, and Division
                     
u = np.array([1, 0])
v = np.array([0, 1])

z = np.add(u, v)
z #output:[1,1]
c = np.subtract(u, v)
c #output: [1,1]
m = np.multiply(u, v)
m #output: [0,0]
d = np.divide(a, b)
d #output:[0,0]


# Plotting functions


import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt


def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)


# Dot Product/////////////////////////////////

X = np.array([1, 2]) 
Y = np.array([3, 2])

# Calculate the dot product
d = np.dot(X, Y) # d = (x[0] * y[0]) + (x[1] * x[2]) / 3+4 = 7 
d #output: 7

# Adding Constant to a Numpy Array ////////////////////////////////////

# Create a constant to numpy array

arr = np.array([1, 2, 3, -1]) 
arr + 5 # Add the constant to array
arr #output: array([6, 7, 8, 4])

# Mathematical Functions /////////////////////////////////////

# The value of pi

np.pi #output: 3.14

# We can create the following numpy array in Radians:
x = np.array([0, np.pi/2 , np.pi])
# We can apply the function sin to the array x and assign the values to the array y;
# this applies the sine function to each element in the array:
# Calculate the sin of each elements
y = np.sin(x)

# Linspace ///////////////////////////////

# A useful function for plotting mathematical functions is linspace. 
# Linspace returns evenly spaced numbers over a specified interval.
# numpy.linspace(start, stop, num = int value)

# Makeup a numpy array within [-2, 2] and 5 elements
np.linspace(-2, 2, num=5) # -22
#output: array([-2., -1.,  0.,  1.,  2.])

# Make a numpy array within [-2, 2] and 9 elements
np.linspace(-2, 2, num=9) # 2 - (-2) = 4 // 4 / 8 = 0.5 // -2,-1.5,-1,-0.5,0,0.5,1,1.5,2
#output: array([-2. , -1.5, -1. , -0.5,  0. ,  0.5,  1. ,  1.5,  2. ])

# Make a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)

# Calculate the sine of x list
y = np.sin(x)

# Plot the result

plt.plot(x, y)


# Import the libraries

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt


def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
    
    
# Convert the list [-1, 1] and [1, 1] to numpy arrays a and b. 
# Then, plot the arrays as vectors using the fuction Plotvec2 and find their dot product:

a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a,b)
print("The dot product is", np.dot(a,b))





