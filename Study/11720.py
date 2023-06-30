import sys

N = int(sys.stdin.readline())
num = list(sys.stdin.readline().strip())

result = 0
for i in num :
    result += int(i)
    
print(result)