# find largest prime factor of 600851475143
import math

def findPrimeFactors(x):
    factors = []
    check = 1
    for y in range(2,int(math.sqrt(x))):
        if(x % y == 0 and isPrime(y)):
            check *= y
            factors.append(y)
            if(check == x):
                print "found"
                break
    return factors

def isPrime(x):
    for y in range(2,x-1):
        if(x % y == 0):
            return False
    return True

print findPrimeFactors(600851475143)[-1]
