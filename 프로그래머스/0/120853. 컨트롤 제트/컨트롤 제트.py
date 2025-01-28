def solution(s):
    answer = 0
    s_list = list(s.split())
    stack = []
    
    for char in s_list:
        if char == 'Z':
            stack.append(-stack[-1])
        else:
            stack.append(int(char))
    
    answer = sum(stack)
    
    return answer