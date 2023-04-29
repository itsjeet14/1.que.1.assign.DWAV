"""Create a random vector of size 30 and find the mean value."""
import numpy as np

vector = np.random.rand(30)
mean_vector = np.mean(vector)
print(vector)
print("Mean Vector: ", mean_vector)