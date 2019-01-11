import time
import math
import numpy as np

ITERATIONS = 10000000

print(f"ITERATIONS:{ITERATIONS}")
start = time.time()
for i in range(ITERATIONS):
    c = complex(i, i)
    abs(c)
end = time.time()
print(f"Time abs(c): {end - start}")

start = time.time()
for i in range(ITERATIONS):
    c = complex(i, i)
    c.real*c.real + c.imag*c.imag
end = time.time()
print(f"Time square: {end - start}")

start = time.time()
for i in range(ITERATIONS):
    c = complex(i, i)
    c.real**2 + c.imag**2
end = time.time()
print(f"Time square2: {end - start}")


start = time.time()
for i in range(ITERATIONS):
    i = i*i
end = time.time()
print(f"Time i*i: {end - start}")


start = time.time()
for i in range(ITERATIONS):
    i = i**2
end = time.time()
print(f"Time i**2: {end - start}")

start = time.time()
for i in range(ITERATIONS):
    i = math.pow(i, 2)
end = time.time()
print(f"Time math.pow(i, 2): {end - start}")

start = time.time()
for i in range(ITERATIONS):
    i = np.square(i)
end = time.time()
print(f"Time np.square(i): {end - start}")
