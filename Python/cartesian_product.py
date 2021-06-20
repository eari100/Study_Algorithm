# 프로그래머스 타겟 넘버

from itertools import product

def solution(numbers, target):
    l = [(x,-x) for x in numbers]
    s = list(map(sum, product(*l)))
    print(s.count(target))

solution([1, 1, 1, 1, 1], 3)