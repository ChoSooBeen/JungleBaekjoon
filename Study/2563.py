import sys

n = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
canvas = [[0]*100 for _ in range(100)]

result = 0
for i in range(n) :
    for j in range(array[i][0], array[i][0]+10) :
        for k in range(array[i][1], array[i][1]+10) :
            if canvas[j][k] == 0 :
                canvas[j][k] = 1
                result += 1
print(result)


# 틀린 풀이 - 계산을 시도한 풀이
# array.sort()
# result = n*100
# for i in range(n) :
#     idx = i+1
#     while idx < n and array[i][0]+10 > array[idx][0]:
#         width = array[idx][0]+10 - array[idx][0] -(array[idx][0]-array[i][0])
#         height = 0
#         if array[i][1] <= array[idx][1] :
#             height = array[i][1]+10 - array[idx][1]
#         else :
#             height = array[idx][1]+10 - array[i][1]
#         result -= width*height
#         idx += 1
# print(result)