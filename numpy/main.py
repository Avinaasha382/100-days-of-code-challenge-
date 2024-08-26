import numpy as np 

#creating a numpy array
a = np.array([1,2,3])
# b = np.array([[1.0,2.0,3.2],[3.4,9.0,10.2]])

# print(a)
# print(b)

# print(type(a),type(b))

# #Getting dimensions of numpy arrays
# print(a.ndim)
# print(b.ndim)

# #Get Shape
# print(a.shape)  # a has 3 rows and is 1 dimensional
# print(b.shape)  #b has 2 rows and each row has 3 columns
# print(b)        #all the elements of the b array
# print(b[:,1])   #accessing the second column of all rows

# #array[startindex:endindex:stepsize] works in accessing array elements as well
# print(b)
# b[1,1] = 10.0
# print(b)

#initialising an array of zeroes:

a = np.zeros((2,2))

b = np.zeros((2,3,2))

c = np.zeros((2,3,3,2))

d = np.ones((4,2),dtype="int32")  #initialises an array of ones

e = np.full((3,3),100)             #initialises an array of 100

#creating an array of random decimal numbers with 4 rows and 2 cols
a = np.random.rand(4,2)  

a = np.random.randint(7,10,(3,3))  #creates a 3x3 matrix with random integers in the range (7,10)
#np.random.randint(start=mandatory,stop=optional,size=tuple/mandatory)

b = np.random.randint(10,size=(4,4))   #if high is none then results are from [0,low) and the dimension is 4x4

i = np.identity(3,dtype="int32")                      #returns a nxn identity matrix

# b = a.copy() creates a new array and assigns to b(pass by value and not reference)

#print(a)

#math and linear algebra operations

# a + 2  adds 2 to all the array elements

# np.sin(array) finds the sin values of all the array elements

# np.matmul(a,b)   multiples matrices a and b given that a[c] = b[r] and output is a[r]b[c]

# np.linalg.det(a)  returns the determinant of the array

# np.sum(array,axis) takes an array as input and outputs the sum. The different cases for a 2D matrix are:
    # --if axis is not specified all array values are summed up
    # -- if axis = 0, then column wise sum
    # -- if axis = 1, then row wise sum



# arr.reshape((dimensions))  pass the dimensions as tuples

# h1 = np.ones((2,3))
# h2 = np.zeros((1,3))  #vertically stacks h2 on h1 and number of columns should be the same

# print(h1)
# print(h2)

# print(np.vstack((h1,h2)))

# h1 = np.ones((2,3))    #horizontally stacks h2 on h1 and number of rows should be same
# h2 = np.zeros((2,5))

# print(h1)
# print(h2)
# print(np.hstack((h1,h2)))

# print(i)

#Loading data from file
# np.genfromtxt(fname="",delimiter="",dtype="") Creates a numpy array from a text file input.
#One should give delimeter in the text file and data type can be specified as default is float.

# arr[arr > 50]  returns an array of elements from arr that are greater than 50.

# IMP -- CHECK OUT np.any(), np.all()

# IMP INSTEAD OF and use & and instead of or use |


np.any(a>50,axis=0)



