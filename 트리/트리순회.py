def preorder(nodes, idx):
  if idx < len(nodes):
    ret = str(nodes[idx]) + " "
    ret += preorder(nodes, 2 * idx + 1)
    ret += preorder(nodes, 2 * idx + 2)
    return ret
  else:
    return ""

def inorder(nodes, idx):
  if idx < len(nodes):    
    ret = inorder(nodes, 2 * idx + 1)
    ret += str(nodes[idx]) + " "
    ret += inorder(nodes, 2 * idx + 2)
    return ret
  else:
    return ""

def postorder(nodes, idx):
  if idx < len(nodes):    
    ret = postorder(nodes, 2 * idx + 1)
    ret += postorder(nodes, 2 * idx + 2)
    ret += str(nodes[idx]) + " "
    return ret
  else:
    return ""
  
def solution(nodes):  
  return [preorder(nodes, 0)[:-1], inorder(nodes, 0)[:-1], postorder(nodes, 0)[:-1]]

print(solution([1, 2, 3, 4, 5, 6, 7]))
