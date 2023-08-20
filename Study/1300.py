import sys

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

start = 1
end = k
result = 0

while start <= end :
    mid = (start+end)//2
    count = 0
    for i in range(1, N+1) :
        count += min(mid//i, N)
    if count < k :
        start = mid + 1
    else :
        end = mid - 1
        result = mid
print(result)