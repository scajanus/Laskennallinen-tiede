from __future__ import division
from pylab import *

def f(x):
    return 1/sqrt(2*pi)*e**(-x**2/2)

def main():
    x = random(100000)
    y = zeros(100000)
    for i in range(0,100000,2):
        y[i] = sqrt(-2*log(x[i]))*cos(2*pi*x[i+1])
        y[i+1] = sqrt(-2*log(x[i]))*sin(2*pi*x[i+1])
    hist(y, bins=100, range=[-5,5], normed=False, weights=None)
    x = arange(-5,5, 0.01)
    plot(x, f(x)*10000, 'r')
    #show()
    Figure=gcf()
    Figure.savefig("gaussian.eps")

if __name__ == "__main__":
    main()

