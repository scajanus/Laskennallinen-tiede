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

def Gauss_part(A, b):
    n = len(A)
    X = zeros((n,1))

    for pivot in range(n-1):
        absm = abs(A[pivot][pivot])
        exchrow = pivot

        for row in range(pivot + 1, n):
            atestm = abs(A[row][pivot])
            if atestm > absm:
                absm = atestm
                exchrow = row

        if pivot != exchrow:
            A[exchrow], A[pivot] = A[pivot], A[exchrow]
            b[exchrow], b[pivot] = b[pivot], b[exchrow]

        m = float(A[pivot][pivot])
        print(m)
        for row in range(pivot +1, n):
            kmul = float(A[row][pivot])/m
            for col in range(n-1, pivot, -1):
                A[row][col] = float(A[row][col]) - kmul * A[pivot][col]
                b[row] = float(b[row]) - kmul * b[pivot]
                A[row][pivot] = 0.0

    for row in range(n-1, -1, -1):
        sum = b[row]
        for k in range(row+1, n):
            sum -= (X[k] * A[row][k])
        X[row] = sum/A[row][row]

    return X



def Gauss_scaled(A):
    k = 0
    n = size(A[1])
    s = zeros((n,1))
    l = zeros((n,1))
    #Create the scaling vector
    for i in range(0,n):
        l[i] = int(i)
        smax = 0
        for j in range(0,n):
            aa = abs(A[i][j])
            if(aa > smax):
                smax = aa
        s[i] = smax
    #print(l)
    #print(s)

    #Loop over steps
    for k in range(0, n-1):
        #Choose pivot equation
        rmax = 0
        j=k
        for i in range (k,n):
            r = abs(A[l[i,0]][k]/s[l[i,0]])
            if(r > rmax):
                rmax = r
            j = i

        #Interchange indeces
        temp = l[j,0]
        l[j,0] = l[k,0]
        l[k,0] = temp

        #Elimination for step k
        for i in range(k+1, n):
            xmult = A[l[i,0]][k]/A[l[k,0]][k]
            A[l[i,0]][k] = xmult
            for j in range(k+1,n):
                A[l[i,0]][j] = A[l[i,0]][j] - xmult*A[l[k,0]][j]
    return A, l

def Solve(A, l, b):
    n = size(l)
    x = zeros((n,1))
    #Determine array bi
    #Elements a[l[i]][k] are the multipliers
    for k in range(0,n-1):
        for i in range(k+1, n):
            b[l[i,0]] = b[l[i,0]]-A[l[i,0]][k]*b[l[k,0]]
    #Back substitution phase
    x[n-1]= b[l[n-1,0]]/A[l[n-1,0]][n-1]
    for i in range(n-2, -1, -1):
        sum = b[l[i,0]]
        for j in range (i+1, n):
            sum = sum - A[l[i,0]][j]*x[j]
        x[i,0] = sum/A[l[i,0]][i]
    return x

def main():
    print("Hello")
    A = hilbert(2)
    b = A.sum(axis=1)
    #print(b)
    print(A)
    A, l = Gauss_scaled(A)
    print(A)
    #x = Solve(A, l, b)
    #print(x)
    #A = hilbert(3)
    #A = array([[1, 2, -1],
            #[-1, -3, 2],
            #[1, -2, 2]])
    #b = A.sum(axis=1)

    #print(Gauss_part(A,b))




if __name__ == "__main__":
    main()
