testcase = int(input())

result = ""
while testcase > 0:
    s = list(input())
    flag = 0
    score = 0
    for c in s :
        if c == 'O' :
            flag += 1
            score += flag
        else :
            flag = 0
    result += f"{score}\n"
    testcase -= 1
print(result)