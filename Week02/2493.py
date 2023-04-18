import sys

N = int(sys.stdin.readline())

tower = list(map(int, sys.stdin.readline().split()))

# 왼쪽부터 탑의 높이를 읽어가기 위해 사용
# 최댓값을 저장할 스택
stack = []

# 수신탑의 인덱스를 저장할 리스트
# 인덱스는 1부터 시작한다.
result = []

for i in range(N) :
    # 스택에 값이 있을 경우
    while stack :
        # 현재 타워 높이 <  왼쪽에 있는 타워 중 가장 높은 타워 높이 
        if tower[stack[-1]] > tower[i] :
            result.append(stack[-1]+1)
            break
        # 아닐경우 -> 현재 타워가 더 높으므로 이 이후에는 스택에 있는 마지막 타워의 높이는 사용 불가
        else :
            stack.pop()
    # 스택에 값이 없을 경우 : 수신이 가능한 탑이 없다.
    if not stack :
        result.append(0)
    # 현재 타워가 수신할 수 있는 경우가 존재하므로 삽입
    stack.append(i)

for i in result :
    print(i, end=" ")