import sys
sys.setrecursionlimit(10**6)

nums = []


# 입력이 더이상 들어오지 않을 때 오류 발생
# 오류가 나타나면 while문 종료
while True :
    try :
        nums.append(int(sys.stdin.readline()))
    except :
        break

# nums의 시작 인덱스 = start
# nums의 끝 인덱스  = end
def post(start, end) :
    if start == end : # start와 end가 같은 경우
        # 한가지 경우만 있으니 출력
        print(nums[start])
        return
    root = nums[start] # 현재 루트 노드
    mid = start
    for i in range(start+1, end+1) :
        if nums[i] > root : # 왼쪽 서브트리와 오른쪽 서브트리 구분을 위한 작업
            mid = i
            break
    if mid == start + 1 or mid == start: # 왼쪽 자식이 없거나 오른쪽 자식이 없으면 
        post(start+1, end)
    else :
        post(start+1, mid-1) # 왼쪽 서브 트리 실행
        post(mid, end) # 오른쪽 서브트리 실행
    print(root) # 마지막으로 루트 출력
        
post(0, len(nums)-1)