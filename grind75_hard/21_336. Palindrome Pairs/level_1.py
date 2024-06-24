# Brute force (Time Limit Exceeded)
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        palindrome_pairs = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                word = words[i] + words[j]
                if word == word[::-1]:
                    palindrome_pairs.append([i, j])
        return palindrome_pairs


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        candidate = {}
        for i, word in enumerate(words):
            candidate[word] = i

        def all_valid_prefixes(word):
            valid_prefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    valid_prefixes.append(word[:i])
            return valid_prefixes

        def all_valid_suffixes(word):
            valid_suffixes = []
            for i in range(len(word)):
                if word[: i + 1] == word[: i + 1][::-1]:
                    valid_suffixes.append(word[i + 1 :])
            return valid_suffixes

        palindrome_pairs = []
        for i, word in enumerate(words):
            reversed_word = word[::-1]
            if reversed_word in candidate and i != candidate[reversed_word]:
                palindrome_pairs.append([candidate[reversed_word], i])

            for suffix in all_valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in candidate:
                    palindrome_pairs.append([candidate[reversed_suffix], i])

            for prefix in all_valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in candidate:
                    palindrome_pairs.append([i, candidate[reversed_prefix]])

        return palindrome_pairs
