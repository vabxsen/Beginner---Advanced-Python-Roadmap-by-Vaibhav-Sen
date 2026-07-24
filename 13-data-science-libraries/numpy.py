"""
=========================================================
Topic : NumPy in Python
=========================================================

This program demonstrates:
1. Creating NumPy Arrays
2. Array Attributes
3. Array Indexing
4. Array Slicing
5. Array Reshaping
6. Mathematical Operations
7. Statistical Functions
8. Random Numbers
9. Sorting Arrays
10. Practical Examples

Install NumPy:
pip install numpy
"""

import numpy as np

print("=" * 60)
print("NUMPY IN PYTHON")
print("=" * 60)

# =======================================================
# CREATING ARRAYS
# =======================================================

print("\n1. Creating Arrays")

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("1D Array:")
print(arr1)

print("\n2D Array:")
print(arr2)

# =======================================================
# ARRAY ATTRIBUTES
# =======================================================

print("\n2. Array Attributes")

print("Dimensions :", arr2.ndim)
print("Shape      :", arr2.shape)
print("Size       :", arr2.size)
print("Data Type  :", arr2.dtype)

# =======================================================
# INDEXING
# =======================================================

print("\n3. Array Indexing")

print("First Element :", arr1[0])
print("Last Element  :", arr1[-1])
print("Element [1][2]:", arr2[1][2])

# =======================================================
# SLICING
# =======================================================

print("\n4. Array Slicing")

print(arr1[1:4])
print(arr2[:, 1:3])

# =======================================================
# RESHAPING
# =======================================================

print("\n5. Reshaping Array")

numbers = np.array([1,2,3,4,5,6])

reshaped = numbers.reshape(2,3)

print(reshaped)

# =======================================================
# MATHEMATICAL OPERATIONS
# =======================================================

print("\n6. Mathematical Operations")

a = np.array([10,20,30])
b = np.array([1,2,3])

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)

# =======================================================
# STATISTICAL FUNCTIONS
# =======================================================

print("\n7. Statistical Functions")

marks = np.array([85,92,78,95,88])

print("Mean   :", np.mean(marks))
print("Median :", np.median(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("Sum    :", np.sum(marks))

# =======================================================
# RANDOM NUMBERS
# =======================================================

print("\n8. Random Numbers")

random_array = np.random.randint(1,101,size=5)

print(random_array)

# =======================================================
# SORTING
# =======================================================

print("\n9. Sorting Arrays")

unsorted = np.array([8,2,5,9,1,7])

print("Original:", unsorted)
print("Sorted  :", np.sort(unsorted))

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n10. Matrix Addition")

matrix1 = np.array([[1,2],[3,4]])
matrix2 = np.array([[5,6],[7,8]])

print(matrix1 + matrix2)

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n11. Identity Matrix")

identity = np.eye(3)

print(identity)

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n12. Zeros and Ones")

zeros = np.zeros((2,3))
ones = np.ones((2,3))

print("Zeros Matrix:")
print(zeros)

print("Ones Matrix:")
print(ones)

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

print("\n13. Even Numbers")

even = np.arange(2,21,2)

print(even)

# =======================================================
# PRACTICAL EXAMPLE 5
# =======================================================

print("\n14. Square Root")

values = np.array([4,9,16,25])

print(np.sqrt(values))

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "="*60)
print("SUMMARY")
print("="*60)

print("1. NumPy provides fast numerical computing.")
print("2. Arrays are faster than Python lists.")
print("3. Supports multi-dimensional arrays.")
print("4. reshape() changes array dimensions.")
print("5. NumPy supports vectorized operations.")
print("6. Provides statistical functions.")
print("7. Random module generates random arrays.")
print("8. NumPy is widely used in AI and Data Science.")
print("9. Used with Pandas, Matplotlib, TensorFlow.")
print("10. Foundation of scientific computing in Python.")

print("\nEnd of Program")