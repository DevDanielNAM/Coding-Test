import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, idx, x, y):
        self.idx = idx
        self.x = x
        self.y = y
        self.left = None
        self.right = None

def insert(parent, child):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            insert(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            insert(parent.right, child)

def preorder(node, result):
    if node:
        result.append(node.idx)
        preorder(node.left, result)
        preorder(node.right, result)

def postorder(node, result):
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.idx)

def solution(nodeinfo):
    nodes = sorted([(idx+1, x, y) for idx, (x, y) in enumerate(nodeinfo)], key=lambda x: (-x[2], x[1]))

    root = Node(*nodes[0])
    for i in range(1, len(nodes)):
        insert(root, Node(*nodes[i]))

    pre_result, post_result = [], []
    preorder(root, pre_result)
    postorder(root, post_result)

    return [pre_result, post_result]
