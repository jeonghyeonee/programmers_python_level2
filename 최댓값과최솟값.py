def solution(s):
    arr = list(map(int, s.split(' ')))     #'-1'과 같은 경우에는 어떻게 받아서 숫자로 변형하지...?
    return '{} {}'.format(min(arr), max(arr))