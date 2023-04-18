import sys

n = int(sys.stdin.readline())

spot = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
spot.sort()

# https://velog.io/@e_juhee/python-백준-2261-가장-가까운-두-점 참고

# 주어진 두 점 사이의 거리 구하는 함수
# 문제의 정답상 거리의 제곱을 구해야 하므로!
def distance(a, b) :
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def fun(start, end) :
    if start == end : # 같으면 거리 계산 불가능
        return sys.maxsize
    elif end - start == 1 : # 단 두점만 가지고 있으면 거리 반환
        return distance(spot[start], spot[end])
    else : # 분할
        mid = (start+end) // 2
        # mid를 기준으로 왼쪽 부분과 오른쪽 부분 계산하여 작은 길이 저장
        tmp = min(fun(start, mid), fun(mid, end))
        
        # 쪼개지는 부분 검증
        candidate = []
        # mid를 기준으로 mid-tmp ~ mid+tmp 범위 내에 존재하는 값을 후보자로 등록
        for i in range(start, end+1) : 
            if (spot[mid][0]-spot[i][0]) ** 2 < tmp :
                candidate.append(spot[i])
        # y값을 기준으로 정렬
        candidate.sort(key=lambda x: x[1])
        # 후보 위치 중에서 범위 내에 존재하면 길이를 구하고 비교
        for i in range(len(candidate)-1) :
            for j in range(i+1, len(candidate)) :
                if (candidate[i][1]-candidate[j][1])**2 < tmp :
                    tmp = min(tmp, distance(candidate[i], candidate[j]))
                else :
                    break
        return tmp
    
print(fun(0, n-1))