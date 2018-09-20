from collections import deque
import copy


with open('problem8set', 'r') as set:
    n = set.read()

def adjacentSum(numberSet):
    product = 1
    for x in numberSet:
       product *= int(x)
    return product

workingSet = deque() 
setLength = 13
highest = -1
highset = []


for number in n :
    try:
        int(number)
        if len(workingSet) < setLength :
            workingSet.append(number)
        if len(workingSet) == setLength :
            check = adjacentSum(workingSet)
            print check, workingSet
            if(check > highest):
                #print check
                highset = copy.copy(workingSet)
                highest = check
            workingSet.popleft()
    except:
        pass
print highest, highset

