class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:

        def make_key(word):
            keys = []
            for i in range(len(word)):
                key = word[:i] + "_" + word[i + 1 :]
                keys.append(key)
            return keys

        word_dict = defaultdict(list)
        for word in wordList:
            keys = make_key(word)
            for key in keys:
                word_dict[key].append(word)

        seen = set([beginWord])
        word_step_queue = deque([(beginWord, 1)])
        while word_step_queue:
            word, step = word_step_queue.popleft()
            keys = make_key(word)
            for key in keys:
                for next_word in word_dict[key]:
                    if next_word == endWord:
                        return step + 1
                    if next_word in seen:
                        continue
                    seen.add(next_word)
                    word_step_queue.append((next_word, step + 1))
        return 0
