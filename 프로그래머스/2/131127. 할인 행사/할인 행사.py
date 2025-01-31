from collections import Counter

def solution(want, number, discount):
    answer = 0
    target = Counter(dict(zip(want, number)))
    current = Counter(discount[:10])
    
    if current == target:
        answer += 1

    for i in range(10, len(discount)):  
        current[discount[i - 10]] -= 1
        if current[discount[i - 10]] == 0:
            del current[discount[i - 10]]
        current[discount[i]] += 1

        if current == target:
            answer += 1

    return answer