# 順番が分かるものについて有向グラフを作成する
# トポロジカルソートのようなことを行う
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjacency_list = defaultdict(set)

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(len(word1)):
                if len(word2) <= j:
                    return ""
                if word1[j] != word2[j]:
                    adjacency_list[word1[j]].add(word2[j])
                    break

        in_degree = {}
        for word in words:
            for c in word:
                in_degree[c] = 0

        for node in adjacency_list:
            for next in adjacency_list[node]:
                in_degree[next] += 1

        output = []
        queue = deque()
        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)

        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adjacency_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        if len(output) < len(in_degree):
            return ""

        return "".join(output)
