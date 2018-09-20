

def Collatz(number):
    count = 1
    while number != 1 :
        count += 1
        if number % 2 == 0 :
            number *= .5
        else :
            number *= 3
            number += 1
    return count

count = 1000000
highest = -1
out = 0

while count > 1 :
    check = Collatz(count)

    if check > highest :
        highest = check
        out = count

    if check == 525 :
        break
    print (count)
    count -= 1
    
print (out) 
