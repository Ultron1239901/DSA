from collections import deque

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right =None

def min_depth(root):
    if root is None:
        return 0
    
    q = deque()
    q.append((root,1))

    while q:
        node, depth = q.popleft()

        if node.left is None and node.right is None:
            return depth
        
        if node.left:
            q.append((node.left, depth+1))

        if node.right:
            q.append((node.right, depth+1))



n = int(input())
nodes = {}
root = None

for _ in range(n):
    value, parent = map(int,input().split())

    if value not in nodes:
        nodes[value] = Node(value)
    child = nodes[value]

    if parent == -1:
        root = child
    else:
        if parent not in nodes:
            nodes[parent] = Node(parent)

        parent_node = nodes[parent]
        if parent_node.left is None:
            parent_node.left = child
        else:
            parent_node.right = child
 
print(min_depth(root)) 