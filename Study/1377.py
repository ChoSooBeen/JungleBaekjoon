import sys

N = int(sys.stdin.readline())
array = [[int(sys.stdin.readline()), i] for i in range(N)]
    
array.sort()
max = -sys.maxsize
for i in range(N) :
    t = array[i][1] - i
    if max < t :
        max = t
print(max+1)