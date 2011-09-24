from __future__ import division
from pylab import *

def coefficients(n, x, y, a):
    a=y;
    for j in arange(1,n+1):
        print j
        for i in linspace(n,j,n-j+1):
            a[i] = (a[i]-a[i-1])/(x[i]-x[i-j])
    return a

def eval(n, x, t, a):
    pt = a[n]
    for i in linspace(n-1,0,n):
        pt = pt * (t-x[i])+a[i];

    return pt


def main():
    print "Hello!"
    x = linspace(0,2,11)
    x_101 = linspace(0,2,101)

    y = exp(x)
    y_101 = exp(x_101)
    a = y
    n = size(x)-1

#plot(x,y)
    a = coefficients(n,x,y,a)
    
    t = linspace(0,2,101)
    y_eval = linspace(0,0,101)

    for i in linspace(0,100,101):
        y_eval[i] = eval(n,x,t[i],a)
    plot(t,abs(y_eval-y_101), 'r')
    show()


if __name__ == "__main__":
    main()
