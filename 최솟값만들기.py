def solution(A,B):
    answer = 0
    
    # A: 내림차순, B: 오름차순 정렬
    A.sort(reverse = True)
    B.sort()
    
    for i in range(len(A)):
        answer += (A[i] * B[i])
    
    return answer

print(solution([1,2], [3,4]))

# 다른 사람의 풀이
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
# zip으로 이렇게 가능한 이유는?