# stacksをdefaultdict(list)を使うことで空の場合の確認を不要にした。
class FreqStack:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.stacks = defaultdict(list)
        self.max_frequency = 0

    def push(self, val: int) -> None:
        self.frequency[val] += 1
        self.max_frequency = max(self.max_frequency, self.frequency[val])
        self.stacks[self.frequency[val]].append(val)

    def pop(self) -> int:
        if not self.stacks[self.max_frequency]:
            return None
        top_value = self.stacks[self.max_frequency].pop()
        self.frequency[val] -= 1
        while self.max_frequency != 0 and not self.stacks[self.max_frequency]:
            self.max_frequency -= 1
        return top_value
