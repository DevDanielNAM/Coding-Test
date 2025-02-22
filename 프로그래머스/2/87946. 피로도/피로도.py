from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0  
    
    for order in permutations(dungeons, len(dungeons)):
        fatigue = k 
        count = 0 

        for min_fatigue, consume in order:
            if fatigue >= min_fatigue:  
                fatigue -= consume  
                count += 1
            else:
                break  

        max_dungeons = max(max_dungeons, count)  
    
    return max_dungeons
