# 7분
from collections import defaultdict

N = int(input())
dic = defaultdict(list)
for i in range(N):
    node, left, right = input().split()
    dic[node] += [left, right]

def preorder(node):
    if node != '.':
        print(node, end = '')
        preorder(dic[node][0])
        preorder(dic[node][1])

def inorder(node):
    if node != '.':
        inorder(dic[node][0])
        print(node, end = '')
        inorder(dic[node][1])

def postorder(node):
    if node != '.':
        postorder(dic[node][0])
        postorder(dic[node][1])
        print(node, end = '')

preorder('A')
print()
inorder('A')
print()
postorder('A')

