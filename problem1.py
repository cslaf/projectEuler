#Find the sum of all the multiples of 3 or 5 below 1000.

answer = 0

for x in range (0, 1000):
    if(x % 5 == 0 or x % 3 == 0):
        answer += x

print answer
