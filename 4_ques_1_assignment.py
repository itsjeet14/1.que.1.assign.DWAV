""" Find indices of non-zero elements from [1,2,0,0,4,0]"""
import numpy as np
lst = [1,2,0,0,4,0]
indeces = np.nonzero(lst)[0]
print(indeces)