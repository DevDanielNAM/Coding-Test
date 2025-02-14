def solution(n, words):
    used_words = set() 
    used_words.add(words[0]) 
    
    for i in range(1, len(words)):
        prev, curr = words[i - 1], words[i]  
        if curr in used_words or prev[-1] != curr[0]: 
            return [(i % n) + 1, (i // n) + 1]  
        used_words.add(curr)
    
    return [0, 0]
