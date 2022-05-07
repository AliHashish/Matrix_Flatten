'''
######## DOCUMENTATION ##########
    Ali Mohamed Ali Hashish
    07/05/2022
    Transforming a 3D matrix into a 1D vector
'''

# Assumptions:
# We are going to fill the vector in a Column major fashion
# meaning that we will take the first column, and place it in the vector
# followed by the second column, and so on. till all the columns on that level
# are finished, then we head to a higher level (higher k), and repeat.

import numpy

# This calculation is done in O(1)
def MatToVec(n,m,p,i,j,k):
    # n,m,p are the dimensions of the Matrix
    # i,j,k are the indices of the 3D Matrix

    Vecindex = i * (m) + j + k * (n * m)
    return Vecindex


# Taking the size as input from user
# n = int(input("Enter 1st dimension size (n): "))
# m = int(input("Enter 2nd dimension size (m): "))
# p = int(input("Enter 3rd dimension size (p): "))
n=3
m=4
p=5
Arr3D = numpy.ones((n, m, p))   # Creating the 3D matrix

# filling the matrix
counter = 0
for i in range(n):
    for j in range(m):
        for k in range(p):
            counter += 1
            Arr3D[i,j,k] = counter


Vec1D = numpy.ones(n*m*p)   # Creating the 1D vector
# Storing the matrix in the vector
for i in range(n):
    for j in range(m):
        for k in range(p):
            index = MatToVec(n, m, p, i, j, k)
            Vec1D[index] = Arr3D[i,j,k]

# Now Vec1D has the elements of Arr3D in a column major fashion



