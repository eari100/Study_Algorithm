from collections import Counter

# 리스트에서 가장 많이 사용된 단어 구하기
def solution1(word_list):
    most_use_word = Counter(word_list).most_common(1)[0][0]
    print(most_use_word)

solution1(['bob', 'a', 'ball', 'the', 'ball', 'flew', 'far', 'after', 'was'])