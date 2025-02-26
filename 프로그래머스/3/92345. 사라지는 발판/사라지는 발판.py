def solution(board, aloc, bloc):
    def dfs(r1, c1, r2, c2, board):
        if board[r1][c1] == 0:
            return (False, 0)
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        can_move = False        
        win_count = float('inf')
        lose_count = 0
        
        for dr, dc in directions:
            nr, nc = r1 + dr, c1 + dc
            
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 1:
                can_move = True                
                board[r1][c1] = 0                
                opponent_win, move_count = dfs(r2, c2, nr, nc, board)                
                board[r1][c1] = 1
                
                if not opponent_win:
                    win_count = min(win_count, move_count + 1)
                else:
                    lose_count = max(lose_count, move_count + 1)
        
        if not can_move:
            return (False, 0)
        
        if win_count != float('inf'):
            return (True, win_count)
        else:
            return (False, lose_count)
    
    _, count = dfs(aloc[0], aloc[1], bloc[0], bloc[1], [row[:] for row in board])
    return count
