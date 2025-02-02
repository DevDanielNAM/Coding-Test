def solution(id_list, report, k):
    reported_by = {id: set() for id in id_list}
    mail_count = {id: 0 for id in id_list}

    for r in report:
        user, reported = r.split()
        reported_by[reported].add(user)

    for reported, users in reported_by.items():
        if len(users) >= k:
            for user in users:
                mail_count[user] += 1

    return list(mail_count.values())