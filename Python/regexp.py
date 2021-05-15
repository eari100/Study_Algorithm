import re

# 정규표현식을 사용하여 문자 형식이외의 문자 제거
def solution1(paragraph: str, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
             .lower().split()
             if word not in banned]

    print(words)

solution1('Bob hit a ball, the hit BALL flew far after it was hit.', 'hit')