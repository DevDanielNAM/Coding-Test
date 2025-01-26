def solution(dirs):
    answer = 0
    start = (0, 0)
    visited = set()

    moves = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    for d in dirs:
        next_pos = (start[0] + moves[d][0], start[1] + moves[d][1])

        if -5 <= next_pos[0] <= 5 and -5 <= next_pos[1] <= 5:
            path = (start, next_pos) if start < next_pos else (next_pos, start)
            visited.add(path)
            start = next_pos
    
    answer = len(visited)
    return answer