from __future__ import division
from pylab import *

def hilbert(n, m=0):
    if n < 1 or m < 0:
        raise ValueError("Matrix size must be one or greater")
    elif n == 1 and (m == 0 or m == 1):
        return np.array([[1]])
    elif m == 0:
       m = n
    return 1. / (np.arange(1, n + 1) + np.arange(0, m)[:, np.newaxis])

def Gauss(A, scaling=0):
    k = 0
    n = size(A[1])
    l = range(n)
    multipliers = zeros((n,n))
    s = ones((n,1))
    #Create the scaling vector, if wanted
    if scaling != 0:
        for i in range(0,n):
            l[i] = int(i)
            smax = 0
            for j in range(0,n):
                aa = abs(A[i][j])
                if(aa > smax):
                    smax = aa
            s[i] = smax
    #Loop over steps
    for k in range(0, n-1):
        #Choose pivot equation
        rmax = 0
        j=k
        for i in range (k,n):
            r = abs(A[l[i]][k]/s[l[i]])
            if(r > rmax):
                rmax = r
                j = i
        #Interchange indeces
        temp = l[j]
        l[j] = l[k]
        l[k] = temp
        #Elimination for step k
        for i in range(k+1, n):
            xmult = A[l[i]][k]/A[l[k]][k]
            multipliers[l[i]][k] = xmult
            A[l[i]] -= xmult * A[l[k]]
    return A, l, multipliers 

def Solve(A, l, b, multipliers):
    n = size(l)
    x = zeros((n,1))
    #Determine array bi
    for k in range(0,n-1):
        for i in range(k+1, n):
            b[l[i]] = b[l[i]]-multipliers[l[i]][k]*b[l[k]]
    #Back substitution phase
    x[n-1]= b[l[n-1]]/A[l[n-1]][n-1]
    for i in range(n-2, -1, -1):
        sum = b[l[i]]
        for j in range (i+1, n):
            sum = sum - A[l[i]][j]*x[j]
        x[i] = sum/A[l[i]][i]
    return x

def main():
    print("Hello")
    for i in range(2,16):
        A = hilbert(i)
        b = A.sum(axis=1)
        A, l, multipliers = Gauss(A, scaling=1)
        x = Solve(A, l, b, multipliers)
        print(transpose(x))

if __name__ == "__main__":
    main()
