def solution(genres, plays):
    answer = []
    g_dic, p_dic = {}, {}
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre not in g_dic:
            g_dic[genre] = []
            p_dic[genre] = 0
        g_dic[genre].append((i, play))
        p_dic[genre] += play
    
    sorted_genres = sorted(p_dic.items(), key = lambda x: x[1], reverse = True)
    
    for genre, _ in sorted_genres:
        sorted_songs = sorted(g_dic[genre], key = lambda x: (-x[1], x[0]))
        answer.extend([idx for idx, _ in sorted_songs[:2]])
    
    return answer