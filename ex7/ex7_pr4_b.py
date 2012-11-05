from __future__ import division
from pylab import *

def f(x):
    return 1/sqrt(2*pi*0.03)*e**(-(x-1/3.0)**2/(2*0.03**2))

def main():
    n=100
    m = 10000
    val = zeros(m)

    for i in range(0,m):
        x = random(n)
        val[i] = mean(x**2)
    hist(val, bins=100, range=[-0.2,0.5], normed=False, weights=None)
    x = arange(-0.1,0.5, 0.005)
    plot(x, f(x)*430, 'r')
    Figure=gcf()
    Figure.savefig("gaussian2.eps")

if __name__ == "__main__":
    main()

