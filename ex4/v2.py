def Gauss_part(A):
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
