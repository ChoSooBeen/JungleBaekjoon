import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    N = int(sys.stdin.readline())
    people = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    # 서류 심사 성적을 기준으로 정렬
    people.sort()
    
    count = 1 # 서류 1등은 우선 무조건 선발 가능
    interview = people[0][1] # 비교할 면접 성적
    for i in range(1, N) :
        # for문의 지원자들은 서류가 1등의 성적보다 무조건 낮기 때문에
        # 적어도 면접 성적이 더 높아야한다.
        if  interview > people[i][1] :
            count += 1
            interview = people[i][1]
    print(count)
