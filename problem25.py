

check = 10**1000

a = 1
b = 1
count = 2

while b < check :
    c = a+b
    a, b = b, c
    count += 1

print(count)

