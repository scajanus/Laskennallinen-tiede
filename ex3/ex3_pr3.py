#from __future__ import division
from pylab import *

def Romberg(f, a, b, n, R):
    kmax=1
    h = b-a
    R[0][0] = (h/2.0)*(f(a)+f(b))
    for i in range(1,n+1):#(i=1 i<=n i++):
        h = h/2.0
        sum = 0
        kmax = kmax*2
        # Trapezoidal estimate R(i,0)
	for k in range(1, kmax, 2):#(k=1 k<=kmax-1 k+=2):
              sum += f(a+k*h)
        R[i][0] = 0.5*R[i-1][0]+sum*h
        # Successive R(i,j)
	for j in range(1,i+1):#(j=1 j<=i j++)
              R[i][j] = R[i][j-1]\
                   +(R[i][j-1]-R[i-1][j-1])/(4.0**j-1.0)

f_test = lambda x: 4.0/(1+x**2)
f_3i = lambda x: 1.0/(1+x)
f_3ii = lambda x: exp(x)
f_3iii = lambda x: sqrt(x)

def main():
    print "Hello!"
    n=5
    R = zeros((n+1,n+1))
#    Romberg(f_test, 0, 1, n, R)
#    for i in range(0,n+1):
#	print '%8.8f %8.8f %8.8f %8.8f %8.8f %8.8f' % tuple(R[i])

    R = zeros((n+1,n+1))
    Romberg(f_3i, 0, 2, n, R)
    for i in range(0,n+1):
	print '%8.8f %8.8f %8.8f %8.8f %8.8f %10.10f' % tuple(R[i])
    print 'True value: %.10f' % log(3)

    R = zeros((n+1,n+1))
    Romberg(f_3ii, 0, 1, n, R)
    for i in range(0,n+1):
	print '%8.8f %8.8f %8.8f %8.8f %8.8f %10.14f' % tuple(R[i])
    print 'True value: %.14f' % (e**1-1)

    n=8
    R = zeros((n+1,n+1))
    a=0; b=1;
    Romberg(f_3iii, a, b, n, R)
    for i in range(0,n+1):
	print '%6.6f %6.6f %6.6f %6.6f %6.6f %6.6f %6.6f %6.6f %10.10f' % tuple(R[i])
    print 'True value: %.10f' % (2.0/3.0*b**(3.0/2.0)-2.0/3.0*a**(3.0/2.0))

    n=8
    R = zeros((n+1,n+1))
    a=0.1; b=1;
    Romberg(f_3iii, a, b, n, R)
    for i in range(0,n+1):
	print '%6.6f %6.6f %6.6f %6.6f %6.6f %6.6f %6.6f %6.6f %10.10f' % tuple(R[i])
    print 'True value: %.10f' % (2.0/3.0*b**(3.0/2.0)-2.0/3.0*a**(3.0/2.0))
#    x=linspace(0.001,1,100)
#    y=1/(2*sqrt(x))
#    xlim(0, 1)
#    plot(x,y, label='1/(2*sqrt(x))')
#    legend()
    
#    show()

if __name__ == "__main__":
    main()
