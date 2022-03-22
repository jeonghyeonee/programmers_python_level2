# https://coding-grandpa.tistory.com/98 

# queue 관련으로 풀 수 있지 않을까????
def solution(priorities, location):
    arr = [(i, p) for i,p in enumerate(priorities)]
    answer = 0
    
    while arr:
        job = arr.pop(0)
        
        if any(job[1] < other_job[1] for other_job in arr):
            arr.append(job)
        
        else:
            answer += 1
            
            if job[0] == location:
                break;
    
    return answer
    

print(solution([2,1,3,2], 2))