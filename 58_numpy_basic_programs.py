
# import for all programs as first line
import numpy as np


# Shape and Reshape Program
arr = np.array(list(map(int, input().split())))
print(np.reshape(arr, (3, 3)))


# Transpose and Flatten
arr = [list(map(int, input().split())) for _ in range(int(input().split()[0]))]
print(np.transpose(np.array(arr)))
print(np.array(arr).flatten())


# Concatenate
m, n, p = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(m)]
arr2 = [list(map(int, input().split())) for _ in range(n)]
print(np.concatenate((arr1, arr2)))


# Zeros and Ones
shape = tuple(map(int, input().split()))
print(np.zeros(shape, dtype=np.int64))
print(np.ones(shape, dtype=np.int64))


# Eye and Identity
np.set_printoptions(legacy='1.13')  # To get the proper alignment while print()
m, n = map(int, input().split())
print(np.eye(m, n, k=0))


# Array Mathematics
n, m = map(int, input().split())
a, b = [np.array([list(map(int, input().split()))
                 for _ in range(n)]) for _ in range(2)]
print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.floor_divide(a, b))
print(np.mod(a, b))
print(np.power(a, b))


# Floor, Ceil and Rint
np.set_printoptions(legacy='1.13')
arr = np.array(list(map(float, input().split())))
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))


# Sum and Prod
n, m = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)])
print(np.prod(np.sum(arr, axis=0)))


# Min and Max
n, m = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)])
print(np.max(np.min(arr, axis=1)))


# Mean, Var, and Std
n, m = map(int, input().split())
arr = np.array([list(map(int, input().split())) for _ in range(n)])
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(round(np.std(arr), 11))


# Dot and Cross
n = int(input())
a, b = [np.array([input().split() for _ in range(n)], int) for _ in range(2)]
b = np.transpose(b)
print(np.array([[np.dot(a[i], b[j]) for j in range(n)] for i in range(n)]))
# OR
n = int(input())
a, b = [np.array([input().split() for _ in range(n)], int) for _ in range(2)]
print(np.dot(a, b))


# Inner and Outer
a, b = [np.array(input().split(), int) for _ in range(2)]
print(np.inner(a, b))
print(np.outer(a, b))


# Polynomials
p = list(map(float, input().split()))
x = int(input())
print(np.polyval(p, x))


# Linear Algebra
n = int(input())
a = np.array([list(map(float, input().split())) for _ in range(n)])
print(round(np.linalg.det(a), 2))
