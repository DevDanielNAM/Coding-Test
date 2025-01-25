def solution(answers):
    answer = []
    
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    correct_cnt = {1:0, 2:0, 3:0}
    
    for i in range(len(answers)):
        if answers[i] == p1[0]:
            correct_cnt[1] += 1
        if answers[i] == p2[0]:
            correct_cnt[2] += 1
        if answers[i] == p3[0]:
            correct_cnt[3] += 1
            
        p1.append(p1.pop(0))
        p2.append(p2.pop(0))
        p3.append(p3.pop(0))
    
    answer = [k for k,v in correct_cnt.items() if max(correct_cnt.values()) == v]
    
    return answer