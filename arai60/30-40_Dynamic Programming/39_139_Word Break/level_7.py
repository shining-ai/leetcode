# ローリングハッシュ
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        prime = 31  # 任意の素数
        m = 10**9 + 9
        prime_pow = [1]
        max_word_length = max(len(word) for word in wordDict)

        for _ in range(max_word_length):
            prime_pow.append((prime_pow[-1] * prime) % m)

        words_hash = set()
        for word in wordDict:
            hash_value = 0
            for i in range(len(word)):
                hash_value = (hash_value + ord(word[i]) * prime_pow[i]) % m
            words_hash.add(hash_value)

        word_end = [False] * len(s)
        for start in range(len(s)):
            if start != 0 and not word_end[start - 1]:
                continue
            target_hash = 0
            for i in range(start, min(start + max_word_length, len(s))):
                target_hash = (target_hash + ord(s[i]) * prime_pow[i - start]) % m
                if target_hash in words_hash:
                    word_end[i] = True
        return word_end[-1]
