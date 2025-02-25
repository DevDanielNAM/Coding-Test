def solution(N):  
  result = []
  
  def backtrack(sum, selected_num, start):
    if sum == 10:
      result.append(selected_num)
      return
  
    for i in range(start, N+1):
      if sum + i <= 10:
        backtrack(sum+i,selected_num+[i], i+1)
  
  backtrack(0,[],1)
  return result
  
N = 5
print(solution(N)) # [[1, 2, 3, 4], [1, 4, 5], [2, 3, 5]]
