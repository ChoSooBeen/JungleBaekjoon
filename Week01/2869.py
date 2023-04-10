A, B, V = input().split()

A = int(A)
B = int(B)
V = int(V)

day = int((V - B) / (A - B))
if (V - B) % (A - B) != 0 :
    day += 1

print(day)