from __future__ import division
from pylab import *

def myexp(x):
    val = 1 + x + x**2/(math.factorial(2)) + x**3/(math.factorial(3)) + x**4/(math.factorial(4))
    return val

def myexpm1(x):
    val = x + x**2/(math.factorial(2)) + x**3/(math.factorial(3)) + x**4/(math.factorial(4))
    return val

def f1(x):
    val=1
    for i in arange(1,100,1):
        val += x**i/(math.factorial(i+1))
    return val

def main():
    print "Let's evaluate!"
    #x = arange(14,16,.10)
    #x = 1*10**-x
    #x = sort(concatenate((-x,x)))
    x = linspace(-1*10**-14,1*10**-14,100)

    y3 = (expm1(x))/x
    print(y3)
    plot(x, y3-y3, 'b')

    y2 = (exp(x)-1)/x
    print(y2)
    plot(x, y2-y3, 'k')

    y4 = (myexpm1(x))/x
    print(y4)
    plot(x, y4-y3, 'g')

    f1values=f1(x)

    xlim(min(x),max(x))
    print "x"
    x=x*10**12
    print x.shape[0]
    for i in arange(1,x.shape[0]):
        print "%.32f" % x[i] + "	" "%.32f" % f1values[i] + "	" "%.32f" % y3[i]
        # + " " + y1+ " " +y2+ " " +y3+ " " + y4
    show()

if __name__ == "__main__":
    main()
