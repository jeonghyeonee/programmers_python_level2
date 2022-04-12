def solution(numbers):
    arr = []
    for i in numbers:
        new_num = i
        while(new_num>=10):
            new_num = i//10
        arr.append(new_num)
    arr.sort
    # 이렇게 풀면 두자리수 이상인 수에 대해서 정확한 결과 얻을 수 없음....
    
    answer = ''
    
    for i in arr:
        answer += str(i)
    
    return answer

print(solution[6, 10, 2])