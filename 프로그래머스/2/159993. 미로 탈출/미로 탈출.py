from collections import deque

def bfs(start, end, maps):
    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True

    dirs = [(0,1), (1,0), (-1,0), (0,-1)] 

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == end:
            return dist

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maps[nx][ny] != "X":
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    return -1

def solution(maps):
    start, lever, exit = None, None, None

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)
            elif maps[i][j] == "E":
                exit = (i, j)

    to_lever = bfs(start, lever, maps)
    if to_lever == -1:
        return -1 

    to_exit = bfs(lever, exit, maps)
    if to_exit == -1:
        return -1

    return to_lever + to_exit
