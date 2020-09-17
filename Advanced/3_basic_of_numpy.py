import numpy as np


# Create an array of ones
print(np.ones((3,4)))

# Create an array of zeros
print(np.zeros((2,3,4),dtype=np.int16))

# Create an empty array
print(np.empty((3,2)))

# Create a full array
print(np.full((2,2),7))

# Create an array of evenly-spaced values
print(np.arange(10,25,5))

# Create an array of evenly-spaced values
print(np.linspace(0,2,9))

x = np.arange(0.0,5.0,1.0)
np.savetxt('test.out', x, delimiter=',')