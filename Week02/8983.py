import sys

# M : 사대 개수
# N : 동물의 수
# L : 사정거리
M, N, L = map(int, sys.stdin.readline().split())

gun = list(map(int, sys.stdin.readline().split())) # 사대의 위치
gun.sort()

animal = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 동물들의 위치

def hunt(gun, animal) :
    count = 0
    # 동물의 위치를 반복
    for x, y in animal :
        min_idx, max_idx = 0, len(gun)-1
        # 동물을 잡을 수 있는 위치를 이분 탐색
        while min_idx <= max_idx :
            mid_idx = (min_idx + max_idx) // 2
            length = abs(gun[mid_idx] - x) + y
            if length <= L :
                count += 1
                break
            else :
                # 동물의 위치보다 사대가 오른쪽에 있으면 max 값 감소
                if gun[mid_idx] > x :
                    max_idx = mid_idx - 1
                # 동물의 x 위치보다 사대가 왼쪽에 있으면 min 값 증가
                else :
                    min_idx = mid_idx + 1
    print(count)        

hunt(gun, animal)