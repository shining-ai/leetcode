# 回数ごとに違うstackを作る
class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.stack = [[]]
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if len(self.stack) < self.freq[val]:
            self.stack.append([])
        self.max_freq = max(self.max_freq, self.freq[val])
        self.stack[self.freq[val] - 1].append(val)

    def pop(self) -> int:
        val = self.stack[self.max_freq - 1].pop()
        self.freq[val] -= 1
        if not self.stack[self.max_freq - 1]:
            self.max_freq -= 1
        return val
