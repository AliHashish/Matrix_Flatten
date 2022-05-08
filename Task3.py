'''
######## DOCUMENTATION ##########
    Ali Mohamed Ali Hashish
    07/05/2022
    Transforming a 3D matrix into a 1D vector

####### EDIT 1 #############
    Used ravel() to flatten the 3D matrix instead
    Reordered the indices to better illustrate the algorithm's accuracy
'''

# Assumptions:
# We are going to fill the vector in a row major fashion
# meaning that we will take the first row, and place it in the vector
# followed by the second row, and so on. till all the row on that level
# are finished, then we head to a higher level (higher k), and repeat.

import numpy

# This calculation is done in O(1)
def MatToVec(n,m,p,i,j,k):
    # n,m,p are the dimensions of the Matrix
    # i,j,k are the indices of the 3D Matrix
    # i: rows
    # j: columns
    # k: levels or stages

    #Vecindex = i * (m) + j + k * (n * m)
    Vecindex = i * (m*p) + j * (p) + k
    return Vecindex


# Taking the size as input from user
n = int(input("Enter 1st dimension size (n): "))
m = int(input("Enter 2nd dimension size (m): "))
p = int(input("Enter 3rd dimension size (p): "))
# n=3
# m=4
# p=5
Arr3D = numpy.ones((n, m, p))   # Creating the 3D matrix


# filling the matrix
counter = 0
for i in range(n):
    for j in range(m):
        for k in range(p):
            counter += 1
            Arr3D[i,j,k] = counter

# print(Arr3D)


Vec1D = Arr3D.ravel()   # Creating the 1D vector by flattening the 3D matrix into 1 row
# print(Vec1D)

# Testing the indexing function
for i in range(n):
    for j in range(m):
        for k in range(p):

            index = MatToVec(n, m, p, i, j, k)
            #print("3D Matrix: ", Arr3D[i,j,k], "    1D Vector: ", Vec1D[index])     # printing to make sure of its validity
            if(Arr3D[i,j,k] != Vec1D[index]):   # prints in case of error
                print("Error!! Mismatching values...")
                print("3D Matrix: ", Arr3D[i, j, k], "    1D Vector: ", Vec1D[index])  # printing to make sure of its validity
                break

# Now Vec1D has the elements of Arr3D in a row major fashion


