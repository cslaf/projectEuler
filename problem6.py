
def sumSquares(x):
    answer = 0
    for x in range(x):
        answer += x*x
    return answer

def squareSum(x):
    answer = 0
    for x in range(x):
        answer += x
    return answer*answer

print squareSum(101) - sumSquares(101)

