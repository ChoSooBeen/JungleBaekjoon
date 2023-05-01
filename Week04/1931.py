import sys

N = int(sys.stdin.readline())
# meeting[0] : 시작 시간 / meeting[1] : 끝나는 시간
meeting = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

meeting.sort(key= lambda x : (x[1], x[0]))

count = 1
prev = meeting[0][1] # 앞 회의 끝나는 시간
for i in range(1, N) :
    # 만약 현재 회의 시작 시간이 앞 회의 시간보다 크거나 같으면
    if prev <= meeting[i][0] :
        count += 1
        prev = meeting[i][1]

print(count)