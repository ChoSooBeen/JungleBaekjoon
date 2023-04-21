import sys

class node :
    def __init__(self, root) :
        self.root = root # 현재 노드
        self.left = None # 왼쪽 자식 노드
        self.right = None # 오른쪽 자식 노드

pre_result = ""
in_result = ""
post_result = ""

# 전위 순회
def preorder(n) :
    global pre_result
    pre_result += n.root
    if n.left != None : 
        preorder(n.left)
    if n.right != None :
        preorder(n.right)

# 중위 순회
def inorder(n) :
    global in_result
    if n.left != None : 
        inorder(n.left)
    in_result += n.root
    if n.right != None :
        inorder(n.right)

# 후위 순회
def postorder(n) :
    global post_result
    if n.left != None : 
        postorder(n.left)
    if n.right != None :
        postorder(n.right)
    post_result += n.root

N = int(sys.stdin.readline()) # 노드의 개수
# A의 아스키 코드 = 65
# 노드는 A ~ Z 까지 가능 
# tree = 노드들의 리스트
tree = [node(chr(i+65)) for i in range(N)]

for _ in range(N) :
    root, left, right = sys.stdin.readline().strip().split()
    # 자식 노드가 존재하면 연결해 주어야 한다.
    if left != '.' and right != '.' : # 양쪽 자식 노드 모두 존재할 때
        tree[ord(root)-65].left = tree[ord(left)-65]
        tree[ord(root)-65].right = tree[ord(right)-65]
    elif left == '.' and right == '.' : # 둘다 없을 때
        continue
    elif left == '.' : # 왼쪽 자식 노드만 없을 때 = 오른쪽 자식 노드만 존재
        tree[ord(root)-65].right = tree[ord(right)-65]
    else : # 오른쪽 자식 노드만 없을 때 = 왼쪽 자식 노드만 존재
        tree[ord(root)-65].left = tree[ord(left)-65]

preorder(tree[0])
inorder(tree[0])
postorder(tree[0])

print(pre_result)
print(in_result)
print(post_result)