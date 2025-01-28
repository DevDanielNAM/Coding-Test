def solution(n, k, cmd):
    deleted = []
    
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]
    
    k += 1
    
    for cmd_i in cmd:
        if cmd_i.startswith('C'):
            deleted.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
        elif cmd_i.startswith('Z'):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
        else:
            action, num = cmd_i.split()
            if action == 'U':
                for _ in range(int(num)):
                    k = up[k]
            if action == 'D':
                for _ in range(int(num)):
                    k = down[k]
    
    answer = ["O"] * n
    for i in deleted:
        answer[i - 1] = "X"
        
    return ''.join(answer)

# def solution(n, k, cmd):
#     answer = 'O' * n
    
#     cur_idx = k
#     stack = []    
#     arr = [i for i in range(n)]
#     origin_arr = arr[::]
    
#     for c in cmd:
#         if len(c) > 1:
#             c1, c2 = map(str, c.split())
#             if c1 == 'U':
#                 cur_idx = (cur_idx - int(c2)) % len(arr)
#             else:
#                 cur_idx = (cur_idx + int(c2)) % len(arr)
            
#         else:
#             c1 = c
#             if c1 == 'C':
#                 stack.append((cur_idx, arr.pop(cur_idx)))
#             else:
#                 z = stack.pop()
#                 arr.insert(z[0], z[1])
                
#     dif = set(origin_arr) - set(arr)
#     answer = list(answer)
#     for d in dif:
#         answer[d] = 'X'
#     answer = ''.join(answer)
    
#     return answer
