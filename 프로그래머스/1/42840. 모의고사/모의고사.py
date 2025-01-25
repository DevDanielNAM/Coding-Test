def solution(answers):
    answer = []
    
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    correct_cnt = {1:0, 2:0, 3:0}
    
    for i, answer in enumerate(answers):
        if answer == p1[i % len(p1)]:
            correct_cnt[1] += 1
        if answer == p2[i % len(p2)]:
            correct_cnt[2] += 1
        if answer == p3[i % len(p3)]:
            correct_cnt[3] += 1
    
    max_score = max(correct_cnt.values())
    answer = [k for k, v in correct_cnt.items() if v == max_score]
    
    return answer