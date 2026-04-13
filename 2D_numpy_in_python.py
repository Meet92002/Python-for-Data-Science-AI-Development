# Create a 2D Numpy Array
# Accessing different elements of a Numpy Array
# Basic Operations

import numpy as np
# Create a list

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a)
# Show the numpy array dimensions
A.ndim #output: 2
# Show the numpy array shape
A.shape #output: (3, 3)
# Show the numpy array size
A.size #output: 9
# Access the element on the second row and third column
A[1, 2] #output: 23
# Access the element on the second row and third column
A[1][2] #output: 23
A[0][0] #output: 11
A[0][0:2] #output: array([11, 12])
A[0:2, 2] #output: array([13, 23])

# Basic Operations///////////////////////////////

# Add X and Y
X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 1], [1, 2]]) 
Z = X + Y
Z #output: ([[3, 1], [1, 3]])

# Multiply Y with 2

Z = 2 * Y
Z #output: ([4, 2], [2, 4])

# Multiply X with Y

Z = X * Y
Z #output: array([[2, 0], [0, 2]])

# Calculate the sine of Z
A = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])
np.sin(Z) #output: array([[0.        , 0.90929743], [0.        , 0.90929743]])

# Create a matrix C

C = np.array([[1,1],[2,2],[3,3]])
# Get the transposed of C in Column converted into Row
C = np.array([[1,1],[2,2],[3,3]])
C.T #output: array([[1, 2, 3], [1, 2, 3]])

# Perform matrix multiplication with the numpy arrays A and B.
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])
mul = np.dot(a, b)
mul #output: array([[ 1,  4], [ 5, 12], [ 9, 20]])
