import collections


# O(n^3) time, O(n) space
def solve_1(s, wordDict):
    words = set(wordDict)
    queue = collections.deque([0])
    seen = set()

    while queue:
        start = queue.popleft()
        if start == len(s):
            return True

        for end in range(start + 1, len(s) + 1):
            if end in seen:
                continue

            if s[start:end] in words:
                queue.append(end)
                seen.add(end)

    return False


# O(n*m) time, O(n) space
def solve_2(s, wordDict):
    def dp(i):
        if i < 0:
            return True

        for word in wordDict:
            if s[i - len(word) + 1 : i + 1] == word and dp(i - len(word)):
                return True

        return False

    return dp(len(s) - 1)


# O(n*m) time, O(n) space
def solve_3(s, wordDict):
    dp = [False for _ in range(len(s) + 1)]

    for i in range(len(s) + 1):
        for word in wordDict:
            if i < len(word):
                continue

            if i == len(word) or dp[i - len(word)]:
                if s[i - len(word) : i] == word:
                    dp[i] = True
                    break

    return dp[-1]


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(solve_1(s, wordDict))
    print(solve_2(s, wordDict))
    print(solve_3(s, wordDict))
