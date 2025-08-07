from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result = []

        for s in str:
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)

        print(anagram_map)
        for value in anagram_map.values():
            result.append(value)
        return result