def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i, price in enumerate(prices):        
        while stack and prices[stack[-1]] > price :
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)
    
    while stack:
        top = stack.pop()
        answer[top] = len(prices) - 1 - top
    
    return answer
