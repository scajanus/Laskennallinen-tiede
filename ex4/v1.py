def Gauss_part(A, b):
    n = len(A)
    X = zeros((n,1))















    for k in range(0, n-1):

	rmax = 0
        j=k
        for i in range(k,n):
            r = abs(A[i][k])
            if(r > rmax):
                rmax = r
                j = i


        if k != j:
            A[j], A[k] = A[k], A[j]
            b[j], b[k] = b[k], b[j]


        for i in range(k +1, n):
            xmult = A[i][k]/A[k][k]
	    A[i][k] = xmult
            for j in range(k+1, n):
                A[i][j] = A[i][j] - xmult * A[k][j]
                b[i] = b[i] - xmult * b[k]
                A[i][k] = 0.0

    for row in range(n-1, -1, -1):
        sum = b[row]
        for k in range(row+1, n):
            sum -= (X[k] * A[row][k])
        X[row] = sum/A[row][row]

    return X
