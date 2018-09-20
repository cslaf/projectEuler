nums = []

with open('problem13set', 'r') as set:
    for line in set:
        line.rstrip('\n')
        nums.append(int(line))


total = 0

for number in nums :
    try:
        total += int(number)
    except:
        pass
print (total)


