from collections import Counter

def solution(N, stages):
    stage_counts = Counter(stages)
    n_person = len(stages)
    f_rate = []

    for i in range(1, N + 1):
        if n_person > 0:
            count = stage_counts[i]
            f_rate.append((i, count / n_person))
            n_person -= count
        else:
            f_rate.append((i, 0))

    return [stage for stage, _ in sorted(f_rate, key=lambda x: (-x[1], x[0]))]

