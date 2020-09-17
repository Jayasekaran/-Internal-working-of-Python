import numpy as np

#NumPy Array
np.random.seed(0)  # seed for reproducibility

x = np.random.randint(10, size=6)  # One-dimensional array
print("One-dimensional array x : ", x)

#Accessing Single Elements
#1. Access all the elements
print (x)

#2. Access first elements
print("# first elements         :", x[0])   
print("# first five elements    :", x[:5])    
print("# every other element, starting at index 1:",x[1::2]) 
print("# all elements, reversed :",x[::-1])  
print("# reversed every other from index 5:",x[5::-2]) 
print("# use negative indices  :", x[-1])

#One-dimensional arrays

#Multi-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

print("# 2-dimensional array x2 : \n", x2)
print("# 3-dimensional array x3 : \n", x3)
print("# x3 ndim  :", x3.ndim)
print("# x3 shape :", x3.shape)
print("# x3 size  :", x3.size)
print("# access by index       : \n",x2[0, 0])
print("# two rows, three columns: \n", x2[:2, :3]) 
print("# all rows, every other column : \n",x2[:3, ::2])  
print("# reversed  all the elements : \n", x2[::-1, ::-1])
print("# first column of x2     : \n", x2[:, 0])  
print("# first row of x2    : \n",x2[0, :])  

# Modified array elements
x2[0, 0] = 12

x2_sub = x2[:2, :2]
print("# extract a 2 x 2 subarray : \n",x2_sub)

x2_sub[0, 0] = 99
print("# modify the sub array element    : \n",x2_sub)   
print("# the subarray change reflects in original array : \n", x2)
    
# Creating copies of arrays
x2_sub_copy = x2[:2, :2].copy()
print("# explicitly copy the data within an array/subarray :\n",x2_sub_copy)

x2_sub_copy[0, 0] = 42
print("# modify the subarray element : \n",x2_sub_copy)
print("# modification in subarray will not touch original array : \n",x2)

# Reshaping of Arrays
grid = np.arange(1, 10)
print("# one-dimensional arrays :",grid)
print("# reshape the 1 dim arry to 3 x 3 array : \n",grid.reshape((3, 3)))

# Concatenation of arrays 1 dim arrays
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = [99, 99, 99]
print("# joining of two arrays     :\n", np.concatenate([x, y, z]))

# Concatenation of arrays 2 dim arrays
grid = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("# concatenate along the first axis   :\n", np.concatenate([grid, grid]))
print("# concatenate along the second axis (0-indexed)  \n:", np.concatenate([grid, grid], axis=1))

# Vertical stack and  horizontal stack functions
x = np.array([1, 2, 3])
y = np.array([[99],
              [99]])
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])
print("# vertically stack the arrays    :\n", np.vstack([x, grid]))
print("# horizontally stack the arrays  :\n",np.hstack([grid, y]))

#Splitting of arrays
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
print("# first element in split x1 : \n",x1,"\n# 2nd element in split x2 : \n", x2,"\n# 3rd element in split x3 : \n", x3)

grid = np.arange(16).reshape((4, 4))
print("# 4 x 4 array        \n:",grid)
upper, lower = np.vsplit(grid, [2])
print("# first element of vsplit  : \n",upper)
print("# 2nd element of vsplit  : \n",lower)

left, right = np.hsplit(grid, [2])
print("# first element in hsplit  : \n",left)
print("# 2nd element in hsplit : \n",right,"\n")

#Trigonometric functions
theta = np.linspace(0, np.pi, 3)
print("# theta      = ", theta)
print("# sin(theta) = ", np.sin(theta))
print("# cos(theta) = ", np.cos(theta))
print("# tan(theta) = ", np.tan(theta))

#Exponents and logarithms
x = [1, 2, 3]
print("# x     =", x)
print("# e^x   =", np.exp(x))
print("# 2^x   =", np.exp2(x))
print("# 3^x   =", np.power(3, x))

x = [1, 2, 4, 10]
print("# x        =", x)
print("# ln(x)    =", np.log(x))
print("# log2(x)  =", np.log2(x))
print("# log10(x) =", np.log10(x))

x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print("# multiply  =", y)

y = np.zeros(10)
np.power(2, x, out=y[::2])
print("# power  =", y)

x = np.arange(1, 6)
print("# x  =", x)
print("# outer products  =\n",np.multiply.outer(x, x))

#Summing the Values in an Array
L = np.random.random(100)
print("# sum of all values in an array:\n",sum(L))

big_array = np.random.rand(1000000)
print("# sum of all values in an array:\n",sum(big_array))
print("# NumPy's version(sum) is computed much more quickly:\n", np.sum(big_array))

print("# min values in an array:\n",min(big_array))
print("# NumPy's version(min) is computed much more quickly:\n", np.min(big_array))
print("# max values in an array:\n",max(big_array))
print("# NumPy's version(max) is computed much more quickly:\n", np.max(big_array))

#binary operations 
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
print("# add array of same size   :\n", a + b)

#array a is stretched, or broadcast across the second dimension in order to match the shape of M
M = np.ones((3, 3))
print("# add a one-dim array to a two-dim array  :\n",M + a)

# Rules of Broadcasting
# Broadcasting in NumPy follows a strict set of rules to determine the interaction between the two arrays:
# Rule 1: If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded with ones on its leading (left) side.
# Rule 2: If the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape.
# Rule 3: If in any dimension the sizes disagree and neither is equal to 1, an error is raised.

##   Broadcasting example 1
# adding a two-dimensional array to a one-dimensional array

M = np.ones((2, 3))
a = np.arange(3)
print("# M.shape = (2, 3):",M.shape)
print("# a.shape = (3,):", a.shape)

# apply rule 1 :array a has fewer dimensions, so we pad it on the left with ones:
# M.shape -> (2, 3)
# a.shape -> (1, 3)
# apply rule 2, we now see that the first dimension disagrees, so we stretch this dimension to match:
# M.shape -> (2, 3)
# a.shape -> (2, 3)

print("# M.shape = (2, 3):",a+M)


 ## Broadcasting example 2
a = np.arange(3).reshape((3, 1))
b = np.arange(3)
print("# a.shape = (3, 1):",a.shape)
print("# b.shape = (3,):", b.shape)

# Apply Rule 1: pad the shape of b with ones:
#a.shape -> (3, 1)
#b.shape -> (1, 3)
#Apply rule 2 tells us that we upgrade each of these ones to match the corresponding size of the other array:
#a.shape -> (3, 3)
#b.shape -> (3, 3)
print("# add arrays, where both arrays need to be broadcast :\n",a + b)

## Broadcasting example 3


## list of other useful functions available in NumPy:

##  Function Name	NaN-safe Version	Description
#   np.sum	        np.nansum	        Compute sum of elements
#   np.prod	        np.nanprod	        Compute product of elements
#   np.mean	        np.nanmean	        Compute mean of elements
#   np.std	        np.nanstd	        Compute standard deviation
#   np.var	        np.nanvar	        Compute variance
#   np.min	        np.nanmin	        Find minimum value
#   np.max	        np.nanmax	        Find maximum value
#   np.argmin	    np.nanargmin	    Find index of minimum value
#   np.argmax	    np.nanargmax	    Find index of maximum value
#   np.median	    np.nanmedian	    Compute median of elements
#   np.percentile	np.nanpercentile	Compute rank-based statistics of elements
#   np.any	        N/A	                Evaluate whether any elements are true
#   np.all	        N/A	                Evaluate whether all elements are true