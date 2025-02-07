def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    idx_map = {name: i for i, name in enumerate(enroll)}

    for s, a in zip(seller, amount):
        revenue = a * 100
        idx = idx_map[s]

        while idx is not None:
            commission = revenue // 10
            answer[idx] += revenue - commission
            revenue = commission

            if revenue < 1:
                break

            parent = referral[idx]
            idx = idx_map[parent] if parent in idx_map else None

    return answer
