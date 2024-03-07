# 幅優先探索
# Time Out
class Solution:
    def ladderLength(self, beginWord, endWord, wordList) -> int:
        seen = set()
        queue = deque()
        queue.append((1, beginWord))

        def is_transformable(word1, word2):
            differ_count = 0
            for c1, c2 in zip(word1, word2):
                if c1 == c2:
                    continue
                differ_count += 1
                if differ_count > 1:
                    return False
            return True

        while queue:
            transformation_num, word = queue.popleft()
            if word == endWord:
                return transformation_num
            seen.add(word)
            for next_word in wordList:
                if next_word in seen:
                    continue
                if not is_transformable(word, next_word):
                    continue
                queue.append((transformation_num + 1, next_word))
        return 0


# 幅優先探索
# 辞書による高速化
class Solution:
    def ladderLength(self, beginWord, endWord, wordList) -> int:
        word_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                key = f"{word[:i]}_{word[i + 1 :]}"
                word_dict[key].append(word)
        seen = set()
        queue = deque()
        queue.append((1, beginWord))
        while queue:
            transformation_num, word = queue.popleft()
            if word == endWord:
                return transformation_num
            seen.add(word)
            for i in range(len(word)):
                key = f"{word[:i]}_{word[i + 1 :]}"
                for next_word in word_dict[key]:
                    if next_word in seen:
                        continue
                    queue.append((transformation_num + 1, next_word))
        return 0
