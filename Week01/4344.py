C = int(input())

result = ""
while C > 0 :
    sum = 0
    s = input().split()
    N = int(s[0])
    for score in s[1:]:
        sum += int(score)
    
    avg = sum / N
    student = 0
    for i in s[1:]:
        if int(i) > avg :
            student += 1
    
    result += "{:.3f}%\n".format(round(student/N * 100, 3))    
    C -= 1

print(result)