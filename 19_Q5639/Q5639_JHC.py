import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break


def buildPostorder(preorder):
    if len(preorder) <= 1:
        return preorder

    parent = preorder[0]

    right_idx = len(preorder)   # 만약 오른쪽 서브트리 없으면 right = [] 되도록.

    for i in range(1, len(preorder)):
        if preorder[i] > parent:
            right_idx = i
            break
    
    left = buildPostorder(preorder[1:right_idx])
    right = buildPostorder(preorder[right_idx:])
    
    postorder = left + right + [parent]
    return postorder

for x in buildPostorder(preorder):
    print(x)