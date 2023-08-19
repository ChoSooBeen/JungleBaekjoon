import sys

k, n = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(k)]
lan.sort()

start = 1
end = lan[k-1]

result = 0
while start <= end :
    mid = (start + end) // 2
    count = 0
    for i in range(k) :
        count += (lan[i] // mid)
    if count < n :
        end = mid - 1
    else :
        start = mid + 1
        if result < mid :
            result = mid
        else :
            break
print(result)