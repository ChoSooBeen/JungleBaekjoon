import sys

N, K = map(int, sys.stdin.readline().split())
num = sys.stdin.readline().strip()

def max_value(num) :
    stack = []
    count = K
    
    for i in range(len(num)) :
        # 스택에 값이 존재하고 현재 값보다 작은 스택 내의 값은 모두 삭제
        while stack and stack[-1] < num[i] and count > 0 :
            stack.pop()
            count -= 1
        stack.append(num[i])
    
    # N-K = 원래 입력값에서 필요한 수 만큼 지운 후의 결과값 길이
    # K번의 지우기 수행을 하지 못했을 경우도 존재 -> 스택의 길이 > 결과값의 길이
    # 스택은 최댓값부터 쌓이도록 했기에 뒤에 필요없는 값 제거
    # ex) 6 2 / 989999
    print(''.join(stack[:N-K]))

max_value(num)
