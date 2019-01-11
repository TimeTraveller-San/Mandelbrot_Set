import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
plt.style.use('dark_background')

def isfinite(c):
    assert isinstance(c, complex), 'invalid value of c'
    n = complex(0, 0)
    iter = 0
    while abs(n) < 10 and iter < 30:
        n = n**2 + c
        iter += 1
    if iter >= 30:
        return True
    return False

def mandelbrot():
    reals = np.linspace(-2, 1, 50000)
    imags = np.linspace(-1, 1, 50000)
    cs = np.array([complex(r, i) for r, i in zip(reals, imags)])
    plot_imags = []
    plot_reals = []
    for real in reals:
        for imag in imags:
            if isfinite(complex(real, imag)):
                plot_reals.append(real)
                plot_imags.append(imag)
    plt.scatter(plot_reals, plot_imags, s=0.01, c='white')
    d = {'fontsize': 8,
             'fontweight' : 1,
             'verticalalignment': 'baseline',
             'horizontalalignment': 'center'
             }

    plt.title("Mandelbrot Set | Time Traveller", fontdict = d)
    plt.axis('off')
    plt.show()
    # plt.savefig('mandelbrot_toodamnveryHQ.png', bbox_inches='tight')

def main():
    figure(num=None, figsize=(9.6, 5.4), dpi=600)
    mandelbrot()

if __name__ == "__main__":
    main()
