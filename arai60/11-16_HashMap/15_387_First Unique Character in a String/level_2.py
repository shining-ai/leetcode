# 1段目のコードから変更なし
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        for i, c in enumerate(s):
            if counts[c] == 1:
                return i
        return -1


# 1段目のコードのリファクタリング
# 2重ループをlistの検索で書き換えた
class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = set()
        for i, c_checking in enumerate(s):
            if c_checking in visited:
                continue
            if c_checking in s[i + 1 :]:
                visited.add(c_checking)
                continue
            return i
        return -1


# linkedhashmapを使った
class LinkedHashMap:
    def __init__(self):
        self.d = collections.OrderedDict()

    def put(self, key, index):
        if key in self.d:
            _ = self.d.pop(key)
        self.d[key] = index

    def pop(self, key):
        if key in self.d:
            index = self.d.pop(key)
            return index

    def pop_top(self):
        if not self.d:
            return -1
        key, index = self.d.popitem(last=False)
        return index


class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = set()
        lhmap = LinkedHashMap()
        for i, c in enumerate(s):
            if c in visited:
                lhmap.pop(c)
                continue
            lhmap.put(c, i)
            visited.add(c)
        return lhmap.pop_top()


# linkedhashmapを使った
# ordereddictを使わずに実装
class ListNode:
    def __init__(self, x):
        self.key = x
        self.next = None
        self.prev = None


class LinkedHashMap:
    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = dict()

    def __add_node(self, key):
        new_node = ListNode(key)
        new_node.next = self.tail
        new_node.prev = self.tail.prev
        new_node.prev.next = new_node
        self.tail.prev = new_node

    def remove_node(self, key):
        node = self.head
        while node:
            if node.key == key:
                break
            node = node.next
        if not node:
            return
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def put(self, key, value):
        if key in self.hashmap:
            self.remove_node(key)
        self.hashmap[key] = value
        self.__add_node(key)

    def pop(self):
        node = self.head.next
        if node.key:
            index = self.hashmap[node.key]
            return index
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = set()
        lhmap = LinkedHashMap()
        for i, c in enumerate(s):
            if c in visited:
                lhmap.remove_node(c)
                continue
            lhmap.put(c, i)
            visited.add(c)
        return lhmap.pop()
