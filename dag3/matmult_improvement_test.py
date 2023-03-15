# Program to multiply two matrices using Numpy
import numpy as np

N = 250

# NxN matrix
X = np.random.randint(0, 100, size=(N, N))

# Nx(N+1) matrix
Y = np.random.randint(0, 100, size=(N, N+1))

# result is Nx(N+1)
result = np.zeros((N, N+1))

# matrix multiplication
result = np.dot(X, Y)

for r in result:
    print(r)
print(result)