def solution(n, computers):
    def dfs(node):
        visited[node] = True
        
        for connected_node in range(n):
            if computers[node][connected_node] == 1 and not visited[connected_node]:
                dfs(connected_node)

    visited = [False] * n 
    network_count = 0 

    for i in range(n):
        if not visited[i]:  
            dfs(i)
            network_count += 1 

    return network_count
