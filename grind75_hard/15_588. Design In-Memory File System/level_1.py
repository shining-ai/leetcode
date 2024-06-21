class TrieNode:
    def __init__(self, name):
        self.name = name
        self.children = defaultdict(None)
        self.isFile = False
        self.content = ""


class FileSystem:

    def __init__(self):
        self.root = TrieNode("/")

    def ls(self, path: str) -> List[str]:
        if path == "/":
            return sorted(self.root.children.keys())
        dirs = path.split("/")[1:]
        node = self.root
        for dir in dirs:
            node = node.children[dir]
        if node.isFile:
            return [node.name]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        dirs = path.split("/")[1:]
        node = self.root
        for dir in dirs:
            if dir not in node.children:
                node.children[dir] = TrieNode(dir)
            node = node.children[dir]

    def addContentToFile(self, filePath: str, content: str) -> None:
        dirs = filePath.split("/")[1:]
        node = self.root
        for dir in dirs:
            if dir not in node.children:
                node.children[dir] = TrieNode(dir)
            node = node.children[dir]
        node.isFile = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        dirs = filePath.split("/")[1:]
        node = self.root
        for dir in dirs:
            node = node.children[dir]
        return node.content
