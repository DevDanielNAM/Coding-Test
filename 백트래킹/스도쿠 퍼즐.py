def solution(board):
  def is_valid(num, row, col):
    return not (in_row(num, row) or in_col(num, col) or in_box(num, row, col))

  def in_row(num, row):
    return num in board[row]

  def in_col(num, col):
    return num in (board[row][col] for row in range(9))

  def in_box(num, row, col):
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    return num in (board[box_row + i][box_col + j] for i in range(3) for j in range(3))

  def find_empty_position():
    for row in range(9):
      for col in range(9):
        if board[row][col] == 0:
          return row, col
    return None

  def find_solution():
    empty_pos = find_empty_position()
    if not empty_pos:
      return True
    row, col = empty_pos
    for num in range(1, 10):
      if is_valid(num, row, col):
        board[row][col] = num
        if find_solution():
          return True
        board[row][col] = 0
    return False

  find_solution()
  return board

board = [
  [5,3,0,0,7,0,0,0,0],
  [6,0,0,1,9,5,0,0,0],
  [0,9,8,0,0,0,0,6,0],
  [8,0,0,0,6,0,0,0,3],
  [4,0,0,8,0,3,0,0,1],
  [7,0,0,0,2,0,0,0,6],
  [0,6,0,0,0,0,2,8,0],
  [0,0,0,4,1,9,0,0,5],
  [0,0,0,0,8,0,0,7,9]
]

print(solution(board))
'''
[
[5, 3, 4, 6, 7, 8, 9, 1, 2], 
[6, 7, 2, 1, 9, 5, 3, 4, 8], 
[1, 9, 8, 3, 4, 2, 5, 6, 7], 
[8, 5, 9, 7, 6, 1, 4, 2, 3], 
[4, 2, 6, 8, 5, 3, 7, 9, 1], 
[7, 1, 3, 9, 2, 4, 8, 5, 6], 
[9, 6, 1, 5, 3, 7, 2, 8, 4], 
[2, 8, 7, 4, 1, 9, 6, 3, 5], 
[3, 4, 5, 2, 8, 6, 1, 7, 9]
]
'''
