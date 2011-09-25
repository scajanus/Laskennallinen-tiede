from __future__ import division
#from __future__ import with_statement
from pylab import *
#from bigfloat import *

def f1_taylor(x): #e^x subsituted by series expansion of 4th degree
    return 1 + x/math.factorial(2) + x**2/math.factorial(3)\
            + x**3/math.factorial(4)

def f1_taylor_100(x): #e^x subsituted by series expansion of 100th degree
    val=1
    for i in arange(1,170,1):
        val += x**i/(math.factorial(i+1))
    return val

def f2_taylor(x): #e^x subsituted by series expansion of 4th degree
    return 1 + x**2/math.factorial(3)

def f2_taylor_100(x): #e^x subsituted by series expansion of 100th degree
    val=1
    for i in arange(1,170,1):
        val += x**i/(math.factorial(i+1))
    return val

def main():
    print "Let's evaluate!"
    x = linspace(-1*10**-8, 1*10**-8, 100)
    f1_taylorv = f1_taylor(x)
    f1_taylorv100 = f1_taylor_100(x)
    f1_true = expm1(x)/x
    f1_without_taylor = (exp(x)-1)/x

    plot(x, f1_taylorv, 'r')
    plot(x, f1_without_taylor, 'b')
    xlim(min(x),max(x))

    #plot(x, abs(f1_taylorv-f1_taylorv100), 'r')
    #plot(x, abs(f1_without_taylor-f1_taylorv100), 'b')
    #ylim(-1*10**-6, 1*10**-4)
    show()

if __name__ == "__main__":
    main()
