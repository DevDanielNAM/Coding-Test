def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)
        elif stack:
            stack.pop()
        else:
            return False

    return not stack