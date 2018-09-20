import math

def numDivisors(num):
    divisors = 2 #every number has 2 divisors
    for prime in primeList :
        if num % prime != 0 :
            return 1
    if(num % 2 == 0):
        divisors += 2
    for x in range(3,int(math.sqrt(num)+1)):
        if(num % x == 0):
            divisors += 2
    return divisors


def isPrime(x):
    for y in range(2,int(math.sqrt(x))+1):
        if(x % y == 0):
            return False
    return True

primeList = []

for x in range(1,5):
    if(isPrime(x)):
        primeList.append(x)
        print (x)


count = 0
number = 0
while True:
    count += 1
    number += count
    divs = numDivisors(number)
    print(number, numDivisors(number))
    if divs > 500 :
        print (number)
        break
    if number > 76576500 :
        print ( "miss" )
        break
    #print (genTri(count), count)

