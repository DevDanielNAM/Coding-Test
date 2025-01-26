def solution(n, left, right):
    answer = []
    
    for k in range(left, right + 1):
        i = k // n
        j = k % n
        answer.append(max(i + 1, j + 1))
    
    return answer