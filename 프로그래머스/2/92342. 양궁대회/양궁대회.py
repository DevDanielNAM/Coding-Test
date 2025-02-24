def solution(n, info):
    from itertools import combinations_with_replacement

    max_diff = 0
    best_case = [-1]

    for case in combinations_with_replacement(range(11), n):
        ryan = [0] * 11
        for idx in case:
            ryan[idx] += 1
        
        ryan_score, apeach_score = 0, 0
        for i in range(11):
            if info[i] == 0 and ryan[i] == 0:
                continue  
            if ryan[i] > info[i]:
                ryan_score += 10 - i
            else:
                apeach_score += 10 - i

        if ryan_score > apeach_score:
            diff = ryan_score - apeach_score
            if diff > max_diff:  
                max_diff = diff
                best_case = ryan[:]
            elif diff == max_diff:  
                if ryan[::-1] > best_case[::-1]:
                    best_case = ryan[:]

    return best_case
