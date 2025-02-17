from collections import defaultdict, deque

def solution(graph, start):
  adj_list = defaultdict(list)
  for u, v in graph:
    adj_list[u].append(v)

  def bfs(start):
    visited = set()
    
    queue = deque([start])
    visited.add(start)
    result.append(start)
    
    while queue:
      node = queue.popleft()
      for neighbor in adj_list.get(node, []):
        if neighbor not in visited:          
          queue.append(neighbor)
          visited.add(neighbor)
          result.append(neighbor)

  result = []
  bfs(start)
  
  return result

graph = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)]
start = 1
print(solution(graph, start))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
