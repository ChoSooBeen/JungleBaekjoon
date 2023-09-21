import sys

s = sys.stdin.readline().strip()
result = ''
stack = []

for ch in s :
    if ord(ch) >= ord('A') and ord(ch) <= ord('Z') :
        result += ch
    else :
        if ch == '(' :
            stack.append(ch)
        elif ch == '*' or ch == '/' :
            while stack and (stack[-1] == '*' or stack[-1] == '/') :
                result += stack.pop()
            stack.append(ch)
        elif ch == '+' or ch == '-' :
            while stack and stack[-1] != '(' :
                result += stack.pop()
            stack.append(ch)
        elif ch == ')' :
            while stack and stack[-1] != '(' :
                result += stack.pop()
            stack.pop()
while stack :
    result += stack.pop()
print(result)