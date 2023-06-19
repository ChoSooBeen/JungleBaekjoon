import sys

N, M = map(int, sys.stdin.readline().split())

lec = list(map(int, sys.stdin.readline().split()))

start = max(lec)
end = sum(lec)

while start <= end :
    size = (start + end) // 2
    blue = [0] * M
    idx = 0
    flag = True
    for j in range(N) :
        if blue[idx] + lec[j] <= size :
            blue[idx] += lec[j]
        else :
            idx += 1
            if idx == M :
                flag = False
                break
            blue[idx] += lec[j]
    if not flag :
        start = size + 1
    else :
        end = size - 1
print(start)