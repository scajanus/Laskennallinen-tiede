from __future__ import division
from pylab import *

def lcg(x, a,b,m):
    return (a*x+b)%m

def main():
    n=10**7
    seed = 560
    #Unif:
    print("Uniform:")
    for i in range(1,4):
        print mean(1/(i+1))

    #LCG:
    print("LCG:")
    x = zeros(n)
    x[0] = seed
    for i in range(1,n):
        x[i] = lcg(x[i-1], 128,0,509)
    x = x/509
    for i in range(1,4):
        print mean(x**i)

    #Mersenne Twister
    print("SRGL:")
    x = random(n)
    for i in range(1,4):
        print mean(x**i)


if __name__ == "__main__":
    main()

