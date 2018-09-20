#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(x):
    x = str(x)
    xrev = []
    xlist = []
    for char in x:
        xlist.append(char)
        xrev.append(char)
    xrev.reverse()
    return xlist == xrev

highest = -1
y = 999

for y in range(1000, 100, -1):
    for x in range(y,100,-1):
        check = x*y 
        if(isPalindrome(check) and check > highest):
            highest = check
print highest
