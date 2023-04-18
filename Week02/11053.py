import sys

# A의 크기
N = int(sys.stdin.readline())
# 수열
A = list(map(int, sys.stdin.readline().split()))

# https://namu.wiki/w/최장%20증가%20부분%20수열#s-3.2 참고

def LIS() :
    # d[i] = A[i]를 마지막 값으로 가지는 가장 긴 증가부분 수열 길이
    d = [A[0]]
    for i in range(1, len(A)) :
        # d에 저장된 가장 마지막 값보다 현재 값이 크면
        if d[-1] < A[i] :
            d.append(A[i])
        # 마지막 값보다 현재 값이 작으면 
        # -> 0 ~ len(d)-1 사이에서 현재값보다 작은 값 중 가장 큰 값을 찾는다  -> 이분탐색
        else :
            min, max = 0, len(d)-1
            save = 0
            while min <= max :
                mid = (min + max) // 2
                if d[mid] < A[i] :
                    min = mid + 1
                else :
                    max = mid -1
                    save = mid
            d[save] = A[i]
    # 최종적으로 구해야하는 값       
    print(len(d))

LIS()