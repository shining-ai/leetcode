# ローリングハッシュ
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        prime = 31  # 任意の素数
        m = 10**9 + 9
        prime_pows = [1]
        max_word_length = max(len(word) for word in wordDict)

        def next_roll_hash(c, hash_value, prime_pow):
            return (hash_value + prime_pow * ord(c)) % m

        for _ in range(max_word_length):
            prime_pows.append((prime_pows[-1] * prime) % m)
        # WordDictの各単語とそのprefixのハッシュ値を計算
        words_hash = set()
        prefix_hash = set()
        for word in wordDict:
            hash_value = 0
            for i in range(len(word)):
                hash_value = next_roll_hash(word[i], hash_value, prime_pows[i])
                prefix_hash.add(hash_value)
            words_hash.add(hash_value)
        # ローリングハッシュで単語分割可能か判定
        word_end = [False] * len(s)
        for start in range(len(s)):
            if start != 0 and not word_end[start - 1]:
                continue
            target_hash = 0
            for i in range(start, min(start + max_word_length, len(s))):
                target_hash = next_roll_hash(s[i], target_hash, prime_pows[i - start])
                if target_hash not in prefix_hash:
                    break
                if target_hash in words_hash:
                    word_end[i] = True
        return word_end[-1]
