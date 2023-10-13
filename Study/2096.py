import sys
n = int(sys.stdin.readline())
x, y, z = map(int, sys.stdin.readline().split())
max_result = [x, y, z]
min_result = [x, y, z]
for _ in range(n-1) :
    current = list(map(int, sys.stdin.readline().split()))
    max_tmp = [0] * 3
    min_tmp = [sys.maxsize] * 3
    for i in range(3) :
        if i-1 >= 0 :
            max_tmp[i] = max(max_result[i-1] + current[i], max_tmp[i])
            min_tmp[i] = min(min_result[i-1] + current[i], min_tmp[i])
        if i+1 < 3 :
            max_tmp[i] = max(max_result[i+1] + current[i], max_tmp[i])
            min_tmp[i] = min(min_result[i+1] + current[i], min_tmp[i])
        max_tmp[i] = max(max_result[i] + current[i], max_tmp[i])
        min_tmp[i] = min(min_result[i] + current[i], min_tmp[i])
    max_result = max_tmp
    min_result = min_tmp
print(max(max_result), min(min_result))