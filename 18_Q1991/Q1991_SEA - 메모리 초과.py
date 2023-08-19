N = int(input())
tree = [None] * (2**26)

root, left, right = input().split()
tree[1] = root
tree[2] = left
tree[3] = right

dic = {}
dic[tree[1]] = 1
if tree[2] != '.':
    dic[tree[2]] = 2
if tree[3] != '.':
    dic[tree[3]] = 3

for i in range(2, N + 1):
    node, left, right = input().split()

    # 부모 노드의 인덱스 구하기
    parent_idx = dic[node]

    # 자식 노드 추가
    tree[2 * parent_idx] = left
    tree[2 * parent_idx + 1] = right

    # 딕셔너리에 추가
    if left != '.':
        dic[left] = 2 * parent_idx 
    
    if right != '.':
        dic[right] = 2 * parent_idx + 1

def preorder(root):
    if tree[root] != '.' and tree[root] != None:
        print(tree[root], end='')
        preorder(2 * root)
        preorder(2 * root + 1)

def inorder(root):
    if tree[root] != '.' and tree[root] != None:
        inorder(2 * root)
        print(tree[root], end='')
        inorder(2 * root + 1)

def postorder(root):
    if tree[root] != '.' and tree[root] != None:
        postorder(2 * root)
        postorder(2 * root + 1)
        print(tree[root], end='')

preorder(1)
print()
inorder(1)
print()
postorder(1)


    
    