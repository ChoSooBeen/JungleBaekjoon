import sys

# https://jih3508.tistory.com/75 참고
def rectangle(l, r) :
    global histogram
    # l,r 이 같은 값을 가리킬 경우 즉, 한개의 히스토그램만 남았을 경우
    # 그 직사각형의 높이가 넓이이다.
    if l == r :
        return histogram[l]
    mid = (l+r)//2 # 현재 가운데 원소
    # 왼쪽 부분과 오른쪽 부분을 분할하여 직사각형의 넓이를 구하면서 큰 값을 area에 저장
    area = max(rectangle(l, mid), rectangle(mid+1, r))
    
    new_left = mid # 왼쪽에서 시작할 시작점 -> l에 맞닿을 때까지 -1
    new_right = mid+1 # 오른쪽에서 시작할 시작점 -> r에 맞닿을 때까지 +1
    height = min(histogram[new_left], histogram[new_right]) # 붙어있는 new_left와 new_right 중 낮은 높이 선택 -> 직사각형 연결
    
    '''
    1. 현재 경계부분이 아닌 왼쪽 또는 오른쪽 부분에서 구한 넓이가 최대인 경우 (코드 10번 줄 참고)
    2. 현재 경계를 기준으로 new_left와 new_right로 만든 직사각형의 넓이가 최대인 경우
    3. 경계의 왼쪽에서 너비 1의 직사각형이 최대인 경우
    4. 경계의 오른쪽에서 너비 1의 직사각형이 최대인 경우
    '''
    area = max(area, height*2, histogram[new_left], histogram[new_right])
    while l < new_left or new_right < r : # 범위 내일 경우
        # 오른쪽 부분이 더 클 경우
        if new_right < r and (new_left <= l or histogram[new_left-1] < histogram[new_right+1]) :
            new_right += 1
            height = min(height, histogram[new_right])
        else :
            new_left -= 1
            height = min(height, histogram[new_left])
        # new_right - new_left + 1 = width  즉, 직사각형의 너비
        area = max(area, height*(new_right-new_left+1))
    return area        
        
while True :
    n, *histogram = map(int, sys.stdin.readline().split())
    if n == 0 :
        break
    print(rectangle(0, n-1))
    

###############스택을 이요한 풀이#################################################
# # https://hooongs.tistory.com/330 참고

# '''
# 직사각형의 최대 넓이를 구하는 함수
# n : 입력받은 직사각형 수
# histogram : 직사각형 높이 정보가 들어있는 리스트
# '''
# def rectangle (n, histogram) :
#     stack = []
#     result = 0
#     for i in range(n) :
#         # 스택의 가장 위에 있는 값이 현재 높이 보다 클 경우
#         while len(stack) != 0 and histogram[stack[-1]] > histogram[i] :
#             t = stack.pop()
#             if len(stack) == 0 :
#                 width = i
#             else :
#                 width = i - stack[-1] - 1
#             result = max(result, histogram[t]*width)
#         stack.append(i)
    
#     # 스택에 아직 값이 남아있을 경우
#     while len(stack) != 0 :
#         t = stack.pop()
#         if len(stack) == 0 :
#             width = n
#         else :
#             width = n - stack[-1] -1
#         result = max(result, histogram[t]*width)
    
#     return result
        
# '''
# 입력값 : (직사각형의 수 + 직사각형들의 높이)가 한줄에 주어진다.
# 입력값[0] = 직사각형의 수
# 입력값[1:] = 직사각형의 높이 
# '''
# while True :
#     histogram = list(map(int, sys.stdin.readline().split()))
#     if histogram[0] == 0:
#         break
#     print(rectangle(histogram[0],histogram[1:]))