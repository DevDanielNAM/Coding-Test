def solution(s):
    answer = 0
    
    stack = []
    p = {')':'(', '}':'{', ']':'['}

    for i in range(len(s)):
        stack.clear()
        if i != 0:
            s = s[1::] + s[0:1]

        for char in s:
            if char in p.values():
                stack.append(char)
            elif stack and p[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(-1)
                break
        if not stack: answer += 1

    return answer