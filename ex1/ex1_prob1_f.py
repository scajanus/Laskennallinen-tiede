from __future__ import division
from pylab import *

def f1_taylor(x): #e^x subsituted by series expansion of 4th degree
    return 1 + x/math.factorial(2) + x**2/math.factorial(3)\
            + x**3/math.factorial(4)

def f2_taylor(x): #e^x subsituted by series expansion of 4th degree
    return 1 + x**2/math.factorial(3)

def main():
    print "Let's evaluate!"
    x = linspace(-1*10**-8, 1*10**-8, 100)

    f1_taylorv = f1_taylor(x)
    f1_without_taylor = (exp(x)-1)/x
    f2_taylorv = f2_taylor(x)
    f2_without_taylor = (exp(x)-exp(-x))/(2*x)

    plot(x, f1_taylorv, 'r')
    plot(x, f1_without_taylor, 'b')
    xlim(min(x),max(x))
    legend(('taylor', '(e^x-1)/x'))
    show()

    x = linspace(-1*10**-6, 1*10**-6, 100)
    plot(x, f2_taylorv, 'r')
    plot(x, f2_without_taylor, 'b')
    xlim(min(x),max(x))
    ylim(.9999999,1.0000001)
    legend(('taylor', '(e^x-e^-x)/(2x)'))
    show()

if __name__ == "__main__":
    main()
