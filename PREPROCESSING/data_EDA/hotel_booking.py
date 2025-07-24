
import numpy as np

# Create a 1D array and a 2D array
array_1d = np.array([1, 2, 3])
array_2d = np.array([[4, 5, 6], [7, 8, 9]])

# Combine them along the second axis (columns)
combined = np.column_stack((array_1d, array_2d))

print("Combined array:")
print(combined)