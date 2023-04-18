import sys

N = int(sys.stdin.readline())

liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()

def search(liquid) :
    left, right = 0,  N-1
    # 최대한 0과 가까운 값 저장
    result = sys.maxsize
    
    # 반환할 값 - 특성값이 0에 가까운 용액을 만들어내는 값들
    result_left, result_right = 0, 0
    
    while left < right :
        # 특성값
        sum = liquid[left] + liquid[right]
        
        # 0에 최대한 가깝게 -> 비교를 쉽게 절댓값 사용
        if abs(sum) < result :
            result = abs(sum)
            result_left, result_right = liquid[left], liquid[right]
            # 특성값이 0이 된 경우
            if sum == 0 :
                return result_left, result_right
        # 특성값이 음수인 경우 -> 음수의 크기를 줄인다.
        if sum < 0 :
            left += 1
        # 양수인 경우 -> 양수의 크기를 줄인다.
        else :
            right -= 1
    return result_left, result_right

l, r = search(liquid)
print(f'{l} {r}')