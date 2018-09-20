import math
def isPrime(x):
    if(x < 10):
        if(x == 2 or x == 3 or x == 5 or x ==7):
            return True
        else:
            return False
    for y in range(2,int((x/2))):
        if(x % y == 0):
            return False
    return True

primeList = []
x = 1
count = 0
while(True):
    x += 1
    if(isPrime(x)):
        count += 1
        print count, x
    if(count >= 10001):
        print "finished",x
        break

