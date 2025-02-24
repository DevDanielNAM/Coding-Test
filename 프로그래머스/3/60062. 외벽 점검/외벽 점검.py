from itertools import permutations

def solution(n, weak, dist):
    weak_length = len(weak)
    extended_weak = weak + [w + n for w in weak]
    
    min_friends = float('inf') 
    
    for start in range(weak_length):
        for friends in permutations(dist):
            count = 1 
            position = extended_weak[start] + friends[count - 1]  
            
            for index in range(start, start + weak_length):
                if extended_weak[index] > position:  
                    count += 1  
                    if count > len(dist):
                        break
                    position = extended_weak[index] + friends[count - 1]  
            
            min_friends = min(min_friends, count) 
    
    return min_friends if min_friends <= len(dist) else -1
