from __future__ import division
from pylab import *

def Simpson(f, a, b, eps, level, level_max, plotlevel):
    print(level)
    h = b-a;
    c = 0.5*(a+b);
    one_simpson = h*(f(a)+4.0*f(c)+f(b))/6.0;

    plt.subplot(plotlevel,1,level+1)
    plot([a,c,b],f(array([a,c,b])))

    d = 0.5*(a+c);
    e = 0.5*(c+b);
    two_simpson = h*(f(a)+4.0*f(d)+2.0*f(c)+4.0*f(e)+f(b))/12.0;
    #Check for level
    if(level+1 >= level_max):
        result = two_simpson;
        print("Maximum level reached");
        print(result)
    else:
    #Check for desired accuracy
        if(fabs(two_simpson-one_simpson) < 15.0*eps):
            result = two_simpson + (two_simpson-one_simpson)/15.0;
        #Divide further
        else:
            left_simpson = Simpson(f,
                    a,c,eps/2.0,level+1,level_max,plotlevel);
            right_simpson = Simpson(f,
                    c,b,eps/2.0,level+1,level_max,plotlevel);
            result = left_simpson + right_simpson;
    return(result)

f_5i = lambda x: 4.0/(1+x**2)
f_5ii = lambda x: cos(2*x)/exp(x)

def main():
    level_max = 30
    epsilon = 0.5*10**-4
    a=0; b=1; plotlevel=2;
    for i in range(1,plotlevel+1):
        plt.subplot(plotlevel,1,i)
        plot(linspace(a,b,100), f_5i(linspace(a,b,100)), 'k')
    ans = Simpson(f_5i, a, b, epsilon, 0, level_max, plotlevel)
    Figure = gcf()
    Figure.set_dpi(600)
    Figure.set_size_inches((7,11))
    Figure.savefig("partition1.eps")
    print(ans)

    clf()

    a=0; b=2*pi; plotlevel=5;
    for i in range(1,plotlevel+1):
        plt.subplot(plotlevel,1,i)
        plot(linspace(a,b,100), f_5ii(linspace(a,b,100)), 'k')

    Figure = gcf()
    ans = Simpson(f_5ii, a, b, epsilon, 0, level_max, plotlevel)
    print(ans)
    Figure.set_dpi(600)
    Figure.set_size_inches((7,11))
    Figure.savefig("partition2.eps")
    #show()

if __name__ == "__main__":
    main()
