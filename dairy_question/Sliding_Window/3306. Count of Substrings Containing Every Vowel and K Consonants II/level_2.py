class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def is_contain_all_vowel(vowel_count):
            for i in vowel_count.values():
                if i <= 0:
                    break
            else:
                return True
            return False

        def at_least_k(word, k):
            vowel_count = {"a": 0, "i": 0, "u": 0, "e": 0, "o": 0}
            left = 0
            right = 0
            consonant_count = 0
            num_valid_substrings = 0

            while right < len(word):
                if word[right] in vowel_count:
                    vowel_count[word[right]] += 1
                else:
                    consonant_count += 1
                while consonant_count >= k and is_contain_all_vowel(vowel_count):
                    num_valid_substrings += len(word) - right
                    c = word[left]
                    if c in vowel_count:
                        vowel_count[c] -= 1
                    else:
                        consonant_count -= 1
                    left += 1
                right += 1
            return num_valid_substrings

        return at_least_k(word, k) - at_least_k(word, k + 1)
