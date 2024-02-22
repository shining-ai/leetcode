# dictのkeyはtupleが使えた
# dict.values()で値を取り出せる
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            anagram_key = sorted(word)
            anagram_map[tuple(anagram_key)].append(word)
        return list(anagram_map.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            char_count = [0] * 26
            for c in word:
                char_count[ord(c) - ord("a")] += 1
            anagram_map[tuple(char_count)].append(word)
        return list(anagram_map.values())
