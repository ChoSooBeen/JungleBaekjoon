import sys

# 입력값 : 뒤에 개행문자 제거
s = sys.stdin.readline().strip()

def getScore(s) :
    stack = [] # (괄호, status : 현재 괄호 속 값)
    score = 0
    
    for i in s :
        # 열린 괄호일 경우
        if i == '(' or i == '[' :
            stack.append({'i': i, 'status':0})
        # 닫힌 괄호이면 스택 안에 무조건 값 존재해야 올바르다.
        elif stack :
            if i == ')' and stack[-1]['i'] == '(':
                current = stack.pop()
                if current['status'] == 0 :
                    if stack :
                        stack[-1]['status'] += 2
                    else :
                        score += 2
                else :
                    if stack :
                        stack[-1]['status'] += 2 * current['status']
                    else :
                        score += 2 * current['status']
            elif i == ']' and stack[-1]['i'] == '[' :
                current = stack.pop()
                if current['status'] == 0 :
                    if stack :
                        stack[-1]['status'] += 3
                    else :
                        score += 3
                else :
                    if stack :
                        stack[-1]['status'] += 3 * current['status']
                    else :
                        score += 3 * current['status']
            # 스택에 올바른 짝으로 존재하지 않았으면 잘못된 경우
            else :
                score = 0
                break
        else :
            score = 0
            break
    print(score)

getScore(s)