import sys

testcase = int(sys.stdin.readline().strip())

def isVPS(input) :
    stack = []
    
    for i in input :
        if i == "(":
            stack.append(i)
        elif i == ")" :
            if stack :
                stack.pop()
            else :
                return "NO"
    if stack :
        return "NO"
    else :
        return "YES"

for i in range(testcase) :
    input = list(sys.stdin.readline())
    print(isVPS(input))