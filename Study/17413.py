import sys

input = sys.stdin.readline().strip()
word = ''
result = ''
flag = True
for ch in input :
    if ch == '<':
        if flag and word:
            result += word[::-1]
            word = ''
        flag = False
        word += ch
    elif ch == '>' :
        word += ch
        result += word
        word = ''
        flag = True
    elif ch == ' ':
        if flag :
            result += word[::-1]
            result += ' '
            word = ''
        else :
            word += ' '
    else :
        word += ch
if word :
    result += word[::-1]
print(result)