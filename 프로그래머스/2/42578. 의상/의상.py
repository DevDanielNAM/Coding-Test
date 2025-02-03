from collections import defaultdict

def solution(clothes):  
    clothes_dict = defaultdict(int)
    print(clothes_dict)

    for _, category in clothes:
        clothes_dict[category] += 1
    print(clothes_dict)

    answer = 1
    for count in clothes_dict.values():
        answer *= (count + 1)

    return answer - 1