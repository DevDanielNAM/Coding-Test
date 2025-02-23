def solution(n):
    def is_valid(queen_positions, new_queen_row, new_queen_col):
        for row, col in enumerate(queen_positions):
            if col == new_queen_col or abs(row - new_queen_row) == abs(col - new_queen_col):
                return False
        return True

    def backtrack(queen_positions, row):
        if row == n:
            return 1 

        count = 0
        for col in range(n):
            if is_valid(queen_positions, row, col):
                count += backtrack(queen_positions + [col], row + 1)

        return count

    return backtrack([], 0)
