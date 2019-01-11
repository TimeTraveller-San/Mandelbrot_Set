'''
Mandelbrot set fractal in python by time traveller
(https://github.com/TimeTraveller-San). For info on Mandelbrot set check out:
https://en.wikipedia.org/wiki/Mandelbrot_set
inside main:
- width, height : width, height of the final rendered image
- max_iter: Maximum number of iterations for each point on the image. An
    iteration stop either after crossing the max_iter or after "escaping" to
    infinity (modulus of complex number = 2)
- cmap is the color map. Check out
    https://matplotlib.org/examples/color/colormaps_reference.html for more
    color maps

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numba import autojit
import time
import os
from matplotlib.pyplot import figure

def check_directory():
    if not os.path.isdir("output"):
        os.makedirs("output")

@autojit #This makes computation much faster
def findEscape(c, max_iter, set):
    z = complex(0, 0)
    i = 0
    while(abs(z)<2 and i < max_iter):
        z = z * z + c
        i += 1
    if i <= max_iter: #It escaped
        set[int(z.real), int(z.imag)] += 1
        return True
    return False #it did not escape

def buddhabrot(height, width, max_iter, name = 'buddhabrot', cmap = 'magma'):
    check_directory()
    im_start, im_end = -1, 1
    re_start, re_end = -2, 1
    set = np.zeros((width, height))
    # xpixels = np.arange(width)
    # ypixels = np.arange(height)
    ignore_x = []
    ignore_y = []
    for _ in range(1000):
        w = np.random.randint(width)
        h = np.random.randint(height)
        if w not in ignore_x and h not in ignore_y:
            escaped = findEscape(complex(w, h), max_iter, set)
            if not escaped:
                ignore_x.append(w)
                ignore_y.append(h)
    print(set)
    filename = f"boutput/{name}_{max_iter}_{cmap}_{width}x{height}.png"
    plt.imsave(filename, set.T, format = "png", cmap = cmap)
    return filename

def main():
    start = time.time()
    figure(dpi = 600)
    width, height = 1920, 1080
    max_iter = 10
    cmap = 'inferno'
    filename = buddhabrot(height, width, max_iter, cmap = cmap)
    end = time.time()
    print(f"{filename} saved in time: {end-start}")

if __name__ == "__main__":
    main()
