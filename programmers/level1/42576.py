# 완주하지 못한 선수

from collections import defaultdict

def solution(participants, completions):
    
    names = defaultdict(int)
    
    for participant in participants :
        names[participant] += 1
    
    for completion in completions :
        names[completion] -= 1

    for name in names.keys() :
        if names[name] == 1 :
            answer = name

    return answer