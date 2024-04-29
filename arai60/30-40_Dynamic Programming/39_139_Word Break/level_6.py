# ローリングハッシュ
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        base = 256
        prime = 919  # 任意の素数

        @cache
        def make_hash(word: str) -> int:
            hash_value = 0
            for i in range(len(word)):
                hash_value += (ord(word[i]) * base ** (len(word) - i - 1)) % prime
            hash_value %= prime
            return hash_value

        max_word_length = max(len(word) for word in wordDict)
        words_hash = set()
        for word in wordDict:
            words_hash.add(make_hash(word))
        word_end = [False] * len(s)
        for start in range(len(s)):
            if start != 0 and not word_end[start - 1]:
                continue
            for end in range(start, min(start + max_word_length, len(s))):
                if make_hash(s[start : end + 1]) in words_hash:
                    word_end[end] = True
        return word_end[-1]
