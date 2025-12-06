"""
Covers:
1. Creating arrays
2. Array properties (shape, size, ndim, dtype)
3. Indexing & slicing
4. Vectorized operations
5. Mathematical functions
6. Boolean filtering
7. Reshaping
8. Stacking arrays
9. Random numbers
"""

import numpy as np

print("\n===== 1. Creating arrays =====")
a = np.array([1, 2, 3, 4])
print("Array a:", a)

b = np.array([[1, 2], [3, 4]])
print("2D array b:\n", b)

zeros = np.zeros((2, 3))
print("Zeros matrix:\n", zeros)

ones = np.ones((3, 2))
print("Ones matrix:\n", ones)

range_arr = np.arange(1, 10, 2)  # start, stop, step
print("Range array:", range_arr)

lin = np.linspace(0, 1, 5)  # 5 evenly spaced numbers
print("Linspace:", lin)


print("\n===== 2. Array Properties =====")
print("b shape:", b.shape)   # rows, columns
print("b size:", b.size)     # total elements
print("b ndim:", b.ndim)     # dimensions
print("b dtype:", b.dtype)   # data type


print("\n===== 3. Indexing & Slicing =====")
arr = np.array([10, 20, 30, 40, 50])
print("arr:", arr)
print("arr[0] =", arr[0])
print("arr[1:4] =", arr[1:4])  # slice index 1 to 3

matrix = np.array([[10, 20, 30],
                   [40, 50, 60]])
print("matrix:\n", matrix)
print("matrix[0, 1] =", matrix[0, 1])  # row 0, col 1
print("matrix[:, 1] =", matrix[:, 1])  # entire column 1
print("matrix[1, :] =", matrix[1, :])  # entire row 1


print("\n===== 4. Vectorized Operations =====")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("x + y =", x + y)
print("x * y =", x * y)
print("x ** 2 =", x ** 2)
print("x + 10 =", x + 10)


print("\n===== 5. Mathematical Functions =====")
nums = np.array([10, 20, 30, 40])
print("sum:", nums.sum())
print("mean:", nums.mean())
print("max:", nums.max())
print("min:", nums.min())
print("std (standard deviation):", nums.std())


print("\n===== 6. Boolean Filtering =====")
data = np.array([10, 50, 30, 5, 80])
print("data:", data)
print("data > 20:", data[data > 20])  # only values > 20
print("data < 50:", data[data < 50])


print("\n===== 7. Reshaping =====")
r = np.arange(1, 10)
print("Original r:", r)
r2 = r.reshape(3, 3)
print("Reshaped to 3x3:\n", r2)


print("\n===== 8. Stacking Arrays =====")
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
print("Vertical stack:\n", np.vstack((a1, a2)))
print("Horizontal stack:\n", np.hstack((a1, a2)))


print("\n===== 9. Random Numbers =====")
print("Random integer 0-9:", np.random.randint(0, 10))
print("Random 1D array:", np.random.rand(5))
print("Random 2D array:\n", np.random.rand(2, 3))
print("Random normal distribution:", np.random.randn(5))
