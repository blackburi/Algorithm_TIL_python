# 혼자 놀기의 달인

def solution(cards):
    
    visited = [False] * (len(cards)+1)
    sizes = []
    
    for i in range(len(cards)) :
        if not visited[i+1] :
            group = []
            cur = i+1
            
            while not visited[cur] :
                visited[cur] = True
                group.append(cur)
                cur = cards[cur-1]
                
            sizes.append(len(group))
    
    sizes.sort()
    
    if len(sizes) < 2 :
        return 0
    return sizes[-1]*sizes[-2]