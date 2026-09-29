class StreamChecker:

    def __init__(self, words: list[str]):
        self.trie = {}
        self.stream = []
        
        for word in words:
            node = self.trie
            for char in reversed(word):
                node = node.setdefault(char, {})
            node['#'] = True

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        node = self.trie
        
        for char in reversed(self.stream):
            if char not in node:
                return False
            node = node[char]
            if '#' in node:
                return True
                
        return False