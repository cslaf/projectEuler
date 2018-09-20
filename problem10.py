import math
def isPrime(x):
    if(x < 10):
        if(x == 2 or x == 3 or x == 5 or x ==7):
            return True
        else:
            return False
    count = 2
    while(count <= math.sqrt(x)):
        if(x % count ==  0):
            return False
        count += 1
    return True

answer = 0
count = 0

for x in range(2000000):
    if( x % 10000 == 0):
        print(x)
    if(isPrime(x)):
        count += 1
        answer += x

print ("count", count)
print (answer)
