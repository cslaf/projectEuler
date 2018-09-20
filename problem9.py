
def isPythagTriplet(numbers):
    return numbers[0]**2 + numbers[1]**2 == numbers[2]**2


check = [1,2,3]
for c in range(0, 1000):
    for b in range(0, 1000-c):
        if(c+b < 1000):
            check[0] = a = 1000 -b -c
            check[1] = b
            check[2] = c
            #if(c % 100 == 0 and b % 100 == 0):
                #print check
            if(isPythagTriplet(check)):
                print a*b*c
