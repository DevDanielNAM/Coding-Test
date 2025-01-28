def solution(s):
    answer = 0
    p = {')': '(', '}': '{', ']': '['}
    n = len(s)

    for i in range(n):
        stack = []
        rotated = s[i:] + s[:i]
        
        for char in rotated:
            if char in p.values():
                stack.append(char)
            elif stack and stack[-1] == p[char]:
                stack.pop()
            else:
                break
        else:
            if not stack:
                answer += 1

    return answer