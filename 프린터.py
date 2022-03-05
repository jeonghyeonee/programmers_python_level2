# queue 관련으로 풀 수 있지 않을까????
def solution(priorities, location):
    answer = 0
    l = len(priorities)
    dic = {}
    for i in range(l):
        dic[chr(65+i)] = priorities[i]
    
    
    return dic

print(solution([2,1,3,2], 2))