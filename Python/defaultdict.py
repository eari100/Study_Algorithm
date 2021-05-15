# 출처 : https://leetcode.com/problems/group-anagrams/submissions/
# defaultdict 자료구조의 활용
def groupAnagrams(strs):
    from collections import defaultdict
    anagrams = defaultdict(list) # default : list

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    print(list(anagrams.values()))
    return list(anagrams.values())


groupAnagrams(["eat","tea","tan","ate","nat","bat"])