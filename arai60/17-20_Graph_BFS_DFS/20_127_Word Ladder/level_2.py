# 幅優先探索
# 隣接リストでできるとコメントを見たので実装した
class Solution:
    def ladderLength(self, beginWord, endWord, wordList) -> int:

        def is_transformable(word1, word2):
            differ_count = 0
            for c1, c2 in zip(word1, word2):
                if c1 == c2:
                    continue
                differ_count += 1
                if differ_count > 1:
                    return False
            return True

        if beginWord not in wordList:
            wordList.append(beginWord)
        adjacency_list = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if is_transformable(wordList[i], wordList[j]):
                    adjacency_list[wordList[i]].append(wordList[j])
                    adjacency_list[wordList[j]].append(wordList[i])

        seen = set([beginWord])
        word_queue = deque([beginWord])
        step = 1
        while word_queue:
            queue_size = len(word_queue)
            step += 1
            for i in range(queue_size):
                word = word_queue.popleft()
                for next_word in adjacency_list[word]:
                    if next_word == endWord:
                        return step
                    if next_word in seen:
                        continue
                    if next_word not in adjacency_list[word]:
                        continue
                    seen.add(next_word)
                    word_queue.append(next_word)
        return 0


# 幅優先探索
# key作成を関数化
class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:

        def get_keys(word):
            keys = []
            for i in range(len(word)):
                keys.append(f"{word[:i]}_{word[i + 1 :]}")
            return keys

        # 1文字異なる単語のペアを辞書に格納
        # 例: {"_ot": ["hot", "dot", "lot"]}
        word_patterns = defaultdict(list)
        for word in wordList:
            keys = get_keys(word)
            for key in keys:
                word_patterns[key].append(word)
        # BFSで最短経路を探索
        seen = set([beginWords])
        word_step_queue = deque([(beginWord, 1)])
        while word_step_queue:
            word, step = word_step_queue.popleft()
            keys = get_keys(word)
            for key in keys:
                for next_word in word_patterns[key]:
                    if next_word == endWord:
                        return step + 1
                    if next_word in seen:
                        continue
                    seen.add(next_word)
                    word_step_queue.append((next_word, step + 1))
        return 0


# 双方向BFS
class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        if endWord not in wordList:
            return 0

        def get_keys(word):
            keys = []
            for i in range(len(word)):
                keys.append(f"{word[:i]}_{word[i + 1 :]}")
            return keys

        # 1文字異なる単語のペアを辞書に格納
        # 例: {"_ot": ["hot", "dot", "lot"]}
        word_patterns = defaultdict(list)
        for word in wordList:
            keys = get_keys(word)
            for key in keys:
                word_patterns[key].append(word)

        def visit_word(queue, seen, others_seen):
            queue_size = len(queue)
            for _ in range(queue_size):
                word = queue.popleft()
                keys = get_keys(word)
                for key in keys:
                    for next_word in word_patterns[key]:
                        if next_word in others_seen:
                            return True
                        if next_word in seen:
                            continue
                        seen.add(next_word)
                        queue.append(next_word)
            return False

        begin_seen = set([beginWord])
        end_seen = set([endWord])
        begin_queue = deque([beginWord])
        end_queue = deque([endWord])
        step = 2
        while begin_queue and end_queue:
            if len(begin_queue) <= len(end_queue):
                main_queue = begin_queue
                main_seen = begin_seen
                other_seen = end_seen
            else:
                main_queue = end_queue
                main_seen = end_seen
                other_seen = begin_seen
            if visit_word(main_queue, main_seen, other_seen):
                return step
            step += 1
        return 0
