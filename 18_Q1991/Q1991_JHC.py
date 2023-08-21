import sys
input = sys.stdin.readline

n = int(input())

graph = {}
for i in range(n):
    node, left, right = map(str, input().split())
    graph[node] = [left, right]

root = 'A'

# 전위순회
def preorder(node):
    if node == '.':
        return
    print(node, end='')
    preorder(graph[node][0])
    preorder(graph[node][1])

# 중위순회
def inorder(node):
    if node == '.':
        return
    inorder(graph[node][0])
    print(node, end='')
    inorder(graph[node][1])

# 후위순회
def postorder(node):
    if node == '.':
        return
    postorder(graph[node][0])
    postorder(graph[node][1])
    print(node, end='')


preorder(root)
print()
inorder(root)
print()
postorder(root)