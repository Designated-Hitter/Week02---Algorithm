import sys
sys.setrecursionlimit(100000)

nodes = []
values = []
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

while True:
    try:
        num = int(input())
        values.append(num)
        nodes.append(Node(num))
    except:
        break

def recur(node, st, en):
    if node == None or en == st:
        return
    
    # 우선 st에서 en까지 중 작은 것과 큰 것의 인덱스 받는다.
    left_node_idx = -1
    right_node_idx = en + 1

    flag1 = False
    flag2 = False

    for i in range(st + 1, en + 1):
        if flag1 and flag2:
            break

        if not flag1 and node.item > values[i]:
            left_node_idx = i
            flag1 = True
        
        if not flag2 and node.item < values[i]:
            right_node_idx = i
            flag2 = True
    
    if left_node_idx != -1:
        node.left = nodes[left_node_idx]
    
    if right_node_idx != en + 1:
        node.right = nodes[right_node_idx]
    
    recur(node.left, left_node_idx, right_node_idx -1)
    recur(node.right, right_node_idx, en)

recur(nodes[0], 0, len(nodes) - 1)

def postorder(node):
    if node != None:
        postorder(node.left)
        postorder(node.right)
        print(node.item)
        
postorder(nodes[0])