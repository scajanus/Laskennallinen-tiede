from __future__ import division
from pylab import *
import string

def spline_coeff(n, t, y):
    z = zeros(n+1); h = zeros(n); b = zeros(n); u = zeros(n); v = zeros(n)

    for i in range(n):
        h[i] = t[i+1] - t[i]
        b[i] = (y[i+1] - y[i])/h[i]
    u[1] = 2.0 * (h[0] + h[1])
    v[1] = 6.0 * (b[1] - b[0])
    for i in range(2,n):
        u[i] = 2.0 * (h[i] + h[i-1]) - h[i-1]*h[i-1]/u[i-1]
        v[i] = 6.0 * (b[i] - b[i-1]) - h[i-1]*v[i-1]/u[i-1]
    for i in range(n-1,0,-1):
        z[i] = (v[i]-h[i]*z[i+1])/u[i]

    return n, t, y, z

def spline_eval(n, t, y, z, x):
    for i in range(n-1,-1,-1):
        if(x-t[i]>=0):
            break;
    h = t[i+1]-t[i]; B = -(h/6.0)*(z[i+1]+2.0*z[i]) + (y[i+1]-y[i])/h
    tmp = 0.5*z[i] + (x-t[i])*(z[i+1]-z[i])/(6.0*h)
    tmp = B + (x-t[i])*tmp
    result = y[i] + (x - t[i])*tmp

    tmp_der = z[i] + 0.5*(x-t[i])*(z[i+1]-z[i])/h
    derivative = B + (x-t[i])*tmp_der
    return result, derivative

f = lambda t: sin(t) + 0.04*t**2
f2 = lambda t: t/(1/4.0+t**2)

def main():
    print("Hello")
    data = open('titanium.dat').readlines()
    data = map(string.strip, data)         
    data = map(string.split, data)         
    t, y = zip(*data)                      
    t = map(float, t)                      
    y = map(float, y)                      
    #t = linspace(-9, 12, 22)
#    t = array([-9.7000, -7.3000, -5.4000, -5.0000, -3.0100, \
#        -2.1300, -1.2000, -0.5600,  0.0000,  1.2000, \
#        4.5000,  6.7000,  9.9000, 10.0000, 12.3000])
#    y = f(t)
#    #print(y)
#    x = linspace(min(t), max(t), 200)
#    y_eval = f(x)
#    y_eval2 = f(x)
#
#    #print(size(t)-1)
#    n, t, y, z = spline_coeff(size(t)-1, t, y)
#    for i in range(size(x)):
#        y_eval2[i] = spline_eval(n, t, y, z, x[i])
#
#    plot(x,y_eval)
#    plot(x,y_eval2)
#    plot(t,y, 'bo')
#    show()
#
#    t = zeros(11)
#    for i in range(-5,6):
#        t[i+5] = tan(i*(pi/12))
    #y = f2(t)
    x = linspace(min(t), max(t), 100)
    y_eval2 = zeros(100)
    y_eval2_derivative = zeros(100)

    n, t, y, z = spline_coeff(size(t)-1, t, y)
    for i in range(size(x)):
        y_eval2[i], y_eval2_derivative[i] = spline_eval(n, t, y, z, x[i])

    plot(x,y_eval2)
    axhline()
    plot(t,y, 'bo')
    xlim((min(t),max(t)))
    Figure=gcf()
    Figure.savefig("function.eps")
    clf()
    plot(x,y_eval2_derivative, 'r')
    xlim((min(t),max(t)))
    Figure=gcf()
    Figure.savefig("derivative.eps")
    #show()
if __name__ == "__main__":
    main()
