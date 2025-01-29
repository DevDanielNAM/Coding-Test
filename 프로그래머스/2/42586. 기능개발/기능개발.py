from collections import deque

def solution(progresses, speeds):
    answer = []
    day = 0
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:
        while progresses[0] + (day * speeds[0]) < 100:
            day += 1
        progresses.popleft()
        speeds.popleft()
        answer.append(1)
        
        while progresses and progresses[0] + (day * speeds[0]) >= 100:
            answer[-1] += 1
            progresses.popleft()
            speeds.popleft()
            
    return answer
