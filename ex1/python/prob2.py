from __future__ import division
from pylab import *

def func(x):
    return x**3-x-5

def func_prime(x):
    return 3*x**2-1


def main():
    x=linspace(-4,4,100)
    x_0=0.57735
    y_0=func(x_0)
    k=func_prime(x_0)
    print(k)
    yvalues=linspace(y_0,y_0,100)-linspace(k,k,100)*(x-linspace(x_0,x_0,100))
    fvalues=func(x)

    plot(x, fvalues, 'k')
    plot(x, yvalues, 'r')
    ylim(-10,10)
    axhline()
    axvline()
    legend(('x^3-x-5', 'tangent at start point'))
    show()



if __name__ == "__main__":
    main()
