import heapq

def solution(N, road, K):
    graph = {i: [] for i in range(1, N + 1)}
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    INF = float('inf')
    distances = {i: INF for i in range(1, N + 1)}
    distances[1] = 0
    
    queue = [(0, 1)]
    
    while queue:
        current_time, current_node = heapq.heappop(queue)
        
        if current_time > distances[current_node]:
            continue
        
        for next_node, time in graph[current_node]:
            new_time = current_time + time
            
            if new_time < distances[next_node]:
                distances[next_node] = new_time
                heapq.heappush(queue, (new_time, next_node))
    
    return sum(1 for d in distances.values() if d <= K)
