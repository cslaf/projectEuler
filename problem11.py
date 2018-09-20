
grid = []
with open('problem11set', 'r') as set:
    for line in set:
        cleaned = line.split(' ')
        cleaned[-1] = cleaned[-1].rstrip('\n')
        grid.append(cleaned)


def sumDir(xIn, yIn):
    highest = -1
    check = 1
    #check right
    if not xIn + 3 > 19 :
        for x in range(xIn, xIn+4) :
            check *= int(grid[yIn][x])
            #if check > highest :
            #    highest = check
        check = 1
    #check down
    if not yIn + 3 > 19 :
        for y in range(yIn, yIn+4) :
            check *= int(grid[y][xIn])
            #if check > highest :
            #    highest = check
        check = 1
    #check downright
    if not yIn + 3 > 19 and not xIn + 3 > 19 :
        for add in range(0,4):
            print (yIn+add, xIn+add)
            print (grid[yIn+add][xIn+add])
            check *= int(grid[yIn+add][xIn+add])
            if check > highest :
                highest = check
        check = 1
    #check downleft
    if not yIn + 3 > 19 and not xIn - 3 < 0 :
        for add in range(0,4):
            check *= int(grid[yIn+add][xIn-add])
            if check > highest :
                highest = check
        check = 1
    return highest

product = 0
location = 1,1
for y in range(20):
    for x in range(20):
        check = int(sumDir(y, x))
        if product < check :
            product = check
            location = y,x

print (product, location)
