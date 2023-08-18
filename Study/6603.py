import sys

def lotto(count, result, num_list) :
    if count == 6 :
        print(*result)
        return
    for i in range(len(num_list)) :
        if num_list[i] not in result :
            result.append(num_list[i])
            lotto(count+1, result, num_list[i+1:])
            result.pop()

while True :
    nums = list(map(int, sys.stdin.readline().split()))
    if nums[0] == 0 :
        break
    lotto(0, [], nums[1:])
    print()