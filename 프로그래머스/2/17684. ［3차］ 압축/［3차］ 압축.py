def solution(msg):
    answer = []
    alpha_dict = {chr(i + 64): i for i in range(1, 27)}
    
    index = 27
    i = 0
    while i < len(msg):
        w = msg[i]
        while i + 1 < len(msg) and w + msg[i + 1] in alpha_dict:
            i += 1
            w += msg[i]

        answer.append(alpha_dict[w])
        if i + 1 < len(msg):
            alpha_dict[w + msg[i + 1]] = index
            index += 1
        
        i += 1
    
    return answer