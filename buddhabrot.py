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
def findEscape(c, max_iter):
    z = complex(0, 0)
    i = 0
    while(abs(z)<2 and i < max_iter):
        z = z*z + c
        i += 1
    return i

def mandelbrot(height, width, max_iter, name = 'mandelbrot', cmap = 'magma'):
    check_directory()
    im_start, im_end = -1, 1
    re_start, re_end = -2, 1
    set = np.zeros((width, height))
    for h, im in enumerate(np.linspace(im_start, im_end, height)):
        for w, re in enumerate(np.linspace(re_start, re_end, width)):
            set[w, h] = findEscape(complex(re, im), max_iter)
    filename = f"output/{name}_{max_iter}_{cmap}_{width}x{height}.png"
    plt.imsave(filename, set.T, format = "png", cmap = cmap)
    return filename

def main():
    start = time.time()
    figure(dpi = 600)
    width, height = 1920, 1080
    max_iter = 100
    cmap = 'inferno'
    filename = mandelbrot(height, width, max_iter, cmap = cmap)
    end = time.time()
    print(f"{filename} saved in time: {end-start}")

if __name__ == "__main__":
    main()
