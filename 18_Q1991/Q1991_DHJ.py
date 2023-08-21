import sys
N = int(sys.stdin.readline())
tree = {} #dictionary 형식
for _ in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right] 
    #tree 라는 dictionary의 key를 root, value를 left, right로 할당
    #{"A": ("b", "c")}
    #b를 인덱싱 하려면 tree['A'][0]

print(tree)

def preorder(root):
    if root != '.':
        print(root, end="") #모든 root인 값 출력
        preorder(tree[root][0]) #left가 root인 경우 찾아서 출력
        preorder(tree[root][1]) #right가 root인 경우 찾아서 출력


def inorder(root):
    if root != '.':
        inorder(tree[root][0]) #모든 left를 찾아서 먼저 재귀
        print(root, end='') 
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end="")

preorder('A')
print() #출력값에 개행을 주기 위한 공백 출력
inorder('A')
print()
postorder('A')
