
def factorial(x):
    ret = 1
    for y in range(2,x+1):
        ret *= y
    return ret

num = str(factorial(100))

total = 0
for n in num :
    total += int(n)

print( total)
