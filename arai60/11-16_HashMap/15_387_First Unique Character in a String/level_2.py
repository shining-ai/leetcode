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
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        unique = collections.OrderedDict()
        for i, c in enumerate(s):
            if c in seen:
                unique.pop(c, None)
                continue
            unique[c] = i
            seen.add(c)
        if not unique:
            return -1
        _, index = unique.popitem(last=False)
        return index


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
        return new_node

    def remove_node(self, key):
        node_info = self.hashmap.pop(key, None)
        if not node_info:
            return
        node = node_info[1]
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def put(self, key, value):
        if key in self.hashmap:
            self.remove_node(key)
        node_address = self.__add_node(key)
        self.hashmap[key] = (value, node_address)

    def pop(self):
        node = self.head.next
        if node.key:
            index, _ = self.hashmap[node.key]
            return index
        return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = set()
        unique = LinkedHashMap()
        for i, c in enumerate(s):
            if c in visited:
                unique.remove_node(c)
                continue
            unique.put(c, i)
            visited.add(c)
        return unique.pop()
