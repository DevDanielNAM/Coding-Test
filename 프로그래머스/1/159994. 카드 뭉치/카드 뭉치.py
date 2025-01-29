from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)    
    
    for c in goal:
        if cards1 and cards1[0] == c:
            cards1.popleft()
        elif cards2 and cards2[0] == c:
            cards2.popleft()
        else:
            return 'No'
    
    return 'Yes'