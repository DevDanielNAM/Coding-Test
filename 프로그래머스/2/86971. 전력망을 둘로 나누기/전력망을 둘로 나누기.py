from collections import deque

def count_nodes(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    count = 1
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]: 
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count

def solution(n, wires):
    min_difference = float('inf')  

    for i in range(len(wires)):
        graph = {i: [] for i in range(1, n+1)}
        for j, (v1, v2) in enumerate(wires):
            if i == j:  
                continue
            graph[v1].append(v2)
            graph[v2].append(v1)

        visited = {i: False for i in range(1, n+1)}
        nodes_count = count_nodes(graph, 1, visited)

        diff = abs((n - nodes_count) - nodes_count)
        min_difference = min(min_difference, diff)

    return min_difference
