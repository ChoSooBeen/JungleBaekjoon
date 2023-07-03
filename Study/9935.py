import sys

s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()
length = len(p)

result = []
for i in s :
    result.append(i)
    if p == ''.join(result[-length:]) :
        for _ in range(length) :
            result.pop()
if len(result) :
    print(''.join(result))
else :
    print("FRULA")