import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

tree.sort()

def treeCut(tree, M) :
    left, right = 0, tree[N-1]
    height = 0
    
    while left <= right :
        # 현재 절단기의 높이
        middle = (left+right) // 2
        
        #현재 높이에서 나무를 잘랐을 때 구할 수 있는 나무 길이
        sum = 0
        for i in tree :
            if i > middle :
                sum += (i - middle)
        
        # 구한 나무의 길이가 필요한 만큼 딱 맞았을 경우
        if sum == M :
            return middle
        # 구한 나무의 길이가 부족할 경우 -> 높이를 낮춰줘야 한다.
        elif sum < M :
            right = middle - 1
        # 구한 나무의 길이가 이미 충분히 많은 경우 -> 높이를 높여야 한다.
        else :
            height = max(height, middle)
            left = middle + 1
            
    return height

print(treeCut(tree, M))