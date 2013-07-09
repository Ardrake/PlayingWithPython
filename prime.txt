import math

def isPrime(n):
    n = abs(int(n))

    if n < 2:
        return False
    if n == 2: 
        return True   
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def showPrimes(n):
    n = abs(int(n))
    
    if n >= 2:
        print 2
    
    for x in range(3, n+1, 2):
        if isPrime(x):
            print x

def maxPrime(n):
    n = abs(int(n))

    if n % 2 == 0:
        lastFactor = 2
        n /= 2
        while n % 2 == 0:
            n /= 2
    else:
        lastFactor = 1

    factor = 3
    maxFactor = math.sqrt(n)
    while n > 1 and factor <= maxFactor:
        if n % factor == 0:
            n /= factor
            lastFactor = factor
            while n % factor == 0:
                n /= factor

            maxFactor = math.sqrt(n)
        factor += 2

    if n == 1:
        return lastFactor
    else:
        return n