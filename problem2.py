
a,b = 0,1
def fibI():
    global a,b
    while True:
        a,b = b, a+b
        yield a

f = fibI()

curr = f.next()

answer = 0

while(curr < 4000000):
    if(curr % 2 == 0):
        answer += curr
    curr = f.next()

print answer
