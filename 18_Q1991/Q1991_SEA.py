N = int(input())

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

"""
알파벳과 인덱스를 매칭하는 배열 혹은 딕셔너리 만든 후
"""
nodes = []
for i in range(N):
    nodes.append(Node(chr(ord('A') + i)))

for i in range(N):
    val, left, right = input().split()

    if left != '.':
        nodes[ord(val) - 65].left = nodes[ord(left) - 65]

    if right != '.':
        nodes[ord(val) - 65].right = nodes[ord(right) - 65]

def preorder(node):
    if node != None:
        print(node.item, end='')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node != None:
        inorder(node.left)
        print(node.item, end='')
        inorder(node.right)

def postorder(node):
    if node != None:
        postorder(node.left) 
        postorder(node.right)
        print(node.item, end='')

preorder(nodes[0])
print()
inorder(nodes[0])
print()
postorder(nodes[0])