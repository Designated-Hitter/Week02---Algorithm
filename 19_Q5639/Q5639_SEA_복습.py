import sys
from collections import defaultdict

sys.setrecursionlimit(100000)
tree = defaultdict(list)
nodes = []

while True:
    try:
        node = int(input())
        nodes.append(node)
    except:
        break


def recur(st, en):
    if st > en:
        return
    
    divided = en + 1

    for i in range(st + 1, en + 1):
        if nodes[i] > nodes[st]:
            divided = i
            break
    
    recur(st + 1, divided - 1)
    recur(divided, en)
    print(nodes[st])
    
recur(0, len(nodes) - 1)