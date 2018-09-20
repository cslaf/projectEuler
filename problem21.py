import math

def isAmicable(x):
    if x == divisors(x):
        return False 
    return x == divisors(divisors(x))

def divisors(x):
    divisors = []

    for num in range(2,int(math.sqrt(x)+2)):
        if x % num == 0 :
            divisors.append(num)
            divisors.append(int(x/num))

    return sum(divisors) + 1

total = 0
for x in range(1,10001) :
    if isAmicable(x):
        print (x)
        total += x

print (divisors(496))
print (total)
