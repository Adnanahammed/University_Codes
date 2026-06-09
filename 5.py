import numpy as np

# 1. Creating 1D and 2D arrays
data_1d = np.array([1, 2, 3, 4, 5])
data_2d = np.random.rand(2, 3)

# 2. Initializing with zeros and ones
zeros_arr = np.zeros(10)
ones_arr = np.ones((3, 4), dtype=np.int32)

# 3. Using arange and reshape
range_data = np.arange(10, 121, 10)
reshaped_data = range_data.reshape(2, 6)

# 4. Array statistics (Sum, Mean, Max, Min)
scores = np.array([[80, 78, 90, 93], 
                   [65, 87, 88, 75],  
                   [98, 100, 68, 80]])

print("Total Sum:", scores.sum())
print("Average:", scores.mean())
print("Maximum:", scores.max())
print("Minimum:", scores.min())

# 5. Finding indexes of max/min values
max_indices = np.argmax(scores, axis=0) # Max per column
min_indices = np.argmin(scores, axis=1) # Min per row