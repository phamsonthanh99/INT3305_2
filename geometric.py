import math

def prob(n, p):
    return 1/(pow(p,n))

def infoMeasure(n, p):
    return -math.log(prob(n,p),2)

def sumProb(N, p):
    i = 0
    sum = 0
    for i in range(1, N+1):
        sum = sum + prob(i, p)
    return sum

def approxEntropy(N, p):
    i = 0
    sum = 0
    averageInfor = 0
    for i in range(1, N+1):
        sum = sum + infoMeasure(i, p)
    averageInfor = sum/N
    return averageInfor
