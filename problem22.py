cleaned = []
with open('problem22set', 'r') as set:
    names = set.read().split(",")
    for n in names :
        cleaned.append(n.strip('"'))


cleaned.sort()

total = 0
count = 0
print(ord('C'))

for name in cleaned :
    count +=1
    for char in name :
        total += (ord(char)-64)*count
print(total)
