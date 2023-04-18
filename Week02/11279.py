import sys

max_heap = [0]

def push(v) :
    max_heap.append(v)
    i = len(max_heap)-1
    parent = i // 2
    while i > 1 :
        if max_heap[parent] < max_heap[i] :
            max_heap[parent], max_heap[i] = max_heap[i], max_heap[parent]
        i = parent
        parent //= 2

def down(idx) :
    left, right = idx*2, idx*2+1
    s = idx
    if left < len(max_heap) and max_heap[left] > max_heap[s] :
        s = left
    if right < len(max_heap) and max_heap[right] > max_heap[s] :
        s = right
    if s != idx :
        max_heap[idx], max_heap[s] = max_heap[s], max_heap[idx]
        down(s)

def heappop() :
    result = max_heap[1]
    max_heap[1] = max_heap[-1]
    max_heap.pop()
    down(1)
    return result

N = int(sys.stdin.readline())

for _ in range(N) :
    i = int(sys.stdin.readline())
    if i == 0 :
        if len(max_heap) == 1 :
            print(max_heap[0])
        else :
            print(heappop())
    else :
        push(i)