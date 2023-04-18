import sys
import heapq

N = int(sys.stdin.readline())

def getScore() :
    card = []
    score = 0
    for _ in range(N) :
        heapq.heappush(card, int(sys.stdin.readline()))
    
    while len(card) > 1 :
        n1 = heapq.heappop(card) # 최솟값1
        n2 = heapq.heappop(card) # 최솟값2
        
        score += (n1+n2) # 현재까지 비교 횟수 누적 저장
        # 위의 합을 힙에 추가
        # 후에 다른 카드와 비교할 때 필요
        heapq.heappush(card, n1+n2) 
    print(score)

getScore()