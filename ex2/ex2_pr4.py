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

def f(x):
    return x/(1/4.0 + x**2)

def main():
    col = ['r', 'b']
    for k in range(2):
        chebysnev = k
        if(chebysnev==0):
            x = linspace(-2.02857, 2.02857, 13)
        else:
            i = linspace(0,12,13)
            x = 2.02857*cos(pi*i/12)
            
        print "Hello!"
        x_101 = linspace(-2.02857, 2.02857, 101)

        y = f(x)
        y_101 = f(x_101)
        a = y
        n = size(x)-1

        a = coefficients(n,x,y,a)

        y_eval = linspace(0,0,101)

        for i in linspace(0,100,101):
            y_eval[i] = eval(n,x,x_101[i],a)
        plot(x_101,abs(y_eval-y_101), col[k])
        #plot(x_101,y_eval, col[k])
    #plot(x_101, y_101, 'k')
    xlim(min(x_101),max(x_101))
    #legend(('approx. using equidistant nodes','approx. using Chebyshev \
#nodes','serpentine curve'),loc=2)
    legend(('approx. using equidistant nodes','approx. using Chebyshev \
nodes'),loc=2)
    show()

if __name__ == "__main__":
    main()
