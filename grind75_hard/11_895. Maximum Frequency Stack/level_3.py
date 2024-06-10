class FreqStack:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.stacks = defaultdict(list)
        self.max_frequency = 0

    def push(self, val: int) -> None:
        self.frequency[val] += 1
        self.stacks[self.frequency[val]].append(val)
        self.max_frequency = max(self.max_frequency, self.frequency[val])

    def pop(self) -> int:
        value = self.stacks[self.max_frequency].pop()
        self.frequency[value] -= 1
        while self.max_frequency != 0 and not self.stacks[self.max_frequency]:
            self.max_frequency -= 1
        return value
