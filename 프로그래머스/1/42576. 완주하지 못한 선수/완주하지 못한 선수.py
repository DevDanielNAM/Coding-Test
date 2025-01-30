def solution(participant, completion):
    p_dict = {}
    
    for p in participant:
        p_dict[p] = p_dict.get(p, 0) + 1
    
    for c in completion:
        p_dict[c] -= 1
        if p_dict[c] == 0:
            del p_dict[c]

    return list(p_dict.keys())[0]