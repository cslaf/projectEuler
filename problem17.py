
def asStrTotal(x) :
    string = ""
    
    if x == 1000 :
        return "onethousand"

    if x >= 100 : 
        string += asStr(int(x/100)) + asStr(100)
        x = x % 100 
        if x != 0 :
            string += "and"
    if x > 20 :    
        string += asStr(x % 10)
        x -= x % 10
    string += asStr(x)
    return string 
        


def asStr(x) :
    nums = {
            0: "",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety",
            100: "hundred",
            1000: "thousand"
            }
    return nums.get(x)

total = 0
for x in range(1,1001):
    print (asStrTotal(x))
    total += len(asStrTotal(x))

print (total)
