
def evenlyDivisible(number):
    x = 1
    while(True):
        x += 1
        if(number % x != 0):
            return x-1

def isPrime(x):
    for y in range(2,x-1):
        if(x % y == 0):
            return False
    return True

x = 1 
top = 21
check = evenlyDivisible(x)
highPrime = [1,1]

for i in range(x, top):
    while(i > check):
       x += 1
       check = evenlyDivisible(x)
    print i, "found", x
