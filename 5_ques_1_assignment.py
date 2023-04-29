"""Create a 10x10 array with random values and find the minimum and maximum values."""
import numpy as np

array = np.random.rand(10,10)
min_arr = np.min(array)
max_arr = np.max(array)
print("Array: ", array)
print("Max value: ", max_arr)
print("Min value: ", min_arr)