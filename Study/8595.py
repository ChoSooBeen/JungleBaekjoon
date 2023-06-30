import sys

n = int(sys.stdin.readline())
words = sys.stdin.readline().strip()

result = 0
number = ''
num = '0123456789'
for w in words :
    if w in num :
        number += w
    elif 0 < len(number) < 7:
        result += int(number)
        number = ''
if 0< len(number) < 7 :
    result += int(number)
print(result)

# 아스키 코드를 사용한 풀이 - 변환과정으로 시간이 더 오래 걸린다.
# import sys

# n = int(sys.stdin.readline())
# words = sys.stdin.readline().strip()

# result = 0
# number = ''
# for w in words :
#     tmp = ord(w)
#     if tmp >= ord('0') and tmp <= ord('9') :
#         number += w
#     elif 0 < len(number) < 7:
#         result += int(number)
#         number = ''
# if 0 < len(number) < 7:
#     result += int(number)
# print(result)