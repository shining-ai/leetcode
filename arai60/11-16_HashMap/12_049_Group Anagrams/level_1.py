# anagramのグループを辞書で管理する
# keyはソートした文字列
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)
        for word in strs:
            sorted_char = sorted(word)
            word_dict["".join(sorted_char)].append(word)
        ans = []
        for key in word_dict:
            ans.append(word_dict[key])
        return ans


# 文字をカウントした値をkeyにする
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            word_dict["".join(str(count))].append(word)
        ans = []
        for key in word_dict:
            ans.append(word_dict[key])
        return ans
