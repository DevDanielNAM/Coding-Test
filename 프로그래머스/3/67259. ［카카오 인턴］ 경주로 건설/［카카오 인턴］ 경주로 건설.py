import heapq

def solution(board):
    N = len(board)
    INF = float('inf')
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    
    heap = []
    heapq.heappush(heap, (0, 0, 0, -1))
    
    while heap:
        cost, x, y, direction = heapq.heappop(heap)
        
        if x == N-1 and y == N-1:
            return cost

        for d, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                new_cost = cost + 100
                
                if direction != -1 and direction != d:
                    new_cost += 500
                
                if new_cost < visited[nx][ny][d]:
                    visited[nx][ny][d] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny, d))

    return -1
