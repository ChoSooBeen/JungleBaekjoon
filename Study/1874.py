import sys

n = int(sys.stdin.readline())
stack = []
result = ''

idx = 1
flag = True
for i in range(n) :
    num = int(sys.stdin.readline())
    for j in range(idx, num+1):
        stack.append(j)
        result += '+\n'
        idx += 1
    if num == stack[-1] :
        stack.pop()
        result += '-\n'
    else :
        flag = False
        break

if flag :
    print(result)
else :
    print('NO')
    
