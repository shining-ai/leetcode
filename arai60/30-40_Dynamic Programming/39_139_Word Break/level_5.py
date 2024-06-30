# trie
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            current = root
            for c in word:
                if c not in current.children:
                    current.children[c] = TrieNode()
                current = current.children[c]
            current.is_word = True

        word_end = [False] * len(s)
        for start in range(len(s)):
            if start != 0 and not word_end[start - 1]:
                continue
            current = root
            for i in range(start, len(s)):
                if s[i] not in current.children:
                    break
                current = current.children[s[i]]
                if current.is_word:
                    word_end[i] = True
        return word_end[-1]


# 正規表現(acceptせず)
# 同じ文字の繰り返しがある場合うまくいかず、修正もできなかった(backtrackingを使えばできそうだが正規表現の意味があまりない?)
# s = "aaaaaaa" wordDict = ["aaaa","aaa"]の場合、正規表現は"(aaa|aaaa)*"となり、"aaaaaaa"にマッチしない
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        pattern = ["("]
        for word in sorted(wordDict):
            pattern.append(re.escape(word))
            pattern.append("|")
        pattern.pop()
        pattern.append(")*")
        return re.match("".join(pattern), s).span() == (0, len(s))


# ローリングハッシュ
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        base = 256
        prime = 109  # 任意の素数

        @cache
        def make_hash(word: str) -> int:
            hash_value = 0
            for i in range(len(word)):
                hash_value += (
                    ord(word[i]) * base ** (len(word) - i - 1)
                ) % prime
            hash_value %= prime
            return hash_value

        hash_list = []
        for word in wordDict:
            hash_value = make_hash(word)
            hash_list.append((len(word), hash_value))

        word_end = [False] * len(s)
        for start in range(len(s)):
            if start != 0 and not word_end[start - 1]:
                continue
            for length, hash_value in hash_list:
                if start + length > len(s):
                    continue
                if hash_value == make_hash(s[start : start + length]):
                    word_end[start + length - 1] = True
        return word_end[-1]
