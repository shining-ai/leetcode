import collections


# timeout
def solve_1(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    def is_transformable(word1, word2):
        diff = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff += 1
        return diff == 1

    net = [set() for _ in range(len(wordList))]
    for i in range(len(wordList)):
        for j in range(i + 1, len(wordList)):
            if is_transformable(wordList[i], wordList[j]):
                net[i].add(j)
                net[j].add(i)

    seen = set()
    queue = collections.deque()
    queue.append((beginWord, 1))
    while queue:
        word, level = queue.popleft()
        if word == endWord:
            return level
        for i in range(len(wordList)):
            if i not in seen and is_transformable(word, wordList[i]):
                queue.append((wordList[i], level + 1))
                seen.add(i)

    return 0


# O(M^2 * N) time complexity
# O(M^2 * N) space complexity
def solve_2(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0

    L = len(beginWord)

    all_combo_dict = collections.defaultdict(list)
    for word in wordList:
        for i in range(L):
            all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

    seen = set()
    queue = collections.deque()
    queue.append((beginWord, 1))

    while queue:
        curr_word, level = queue.popleft()
        for i in range(L):
            intermediate_word = curr_word[:i] + "*" + curr_word[i + 1 :]
            for word in all_combo_dict[intermediate_word]:
                if word == endWord:
                    return level + 1
                if word not in seen:
                    queue.append((word, level + 1))
                    seen.add(word)
            all_combo_dict[intermediate_word] = []

    return 0


from collections import defaultdict


def solve_3(beginWord, endWord, wordList):
    length = 0
    all_combo_dict = defaultdict(list)

    def visitWordNode(queue, visited, others_visited):
        queue_size = len(queue)
        for _ in range(queue_size):
            current_word = queue.popleft()
            for i in range(length):
                intermediate_word = (
                    current_word[:i] + "*" + current_word[i + 1 :]
                )

                for word in all_combo_dict[intermediate_word]:
                    if word in others_visited:
                        return visited[current_word] + others_visited[word]
                    if word not in visited:
                        visited[word] = visited[current_word] + 1
                        queue.append(word)

        return None

    if endWord not in wordList:
        return 0

    length = len(beginWord)

    for word in wordList:
        for i in range(length):
            all_combo_dict[word[:i] + "*" + word[i + 1 :]].append(word)

    queue_begin = collections.deque([beginWord])
    queue_end = collections.deque([endWord])

    visited_begin = {beginWord: 1}
    visited_end = {endWord: 1}
    ans = None

    while queue_begin and queue_end:
        if len(queue_begin) <= len(queue_end):
            ans = visitWordNode(queue_begin, visited_begin, visited_end)
        else:
            ans = visitWordNode(queue_end, visited_end, visited_begin)
        if ans:
            return ans

    return 0


if __name__ == "__main__":
    strs = ["hot", "dot", "dog", "lot", "log", "cog"]
    beginWord = "hit"
    endWord = "cog"
    print(solve_1(beginWord, endWord, strs))
    print(solve_2(beginWord, endWord, strs))
    print(solve_3(beginWord, endWord, strs))
