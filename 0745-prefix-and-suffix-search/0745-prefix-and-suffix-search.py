class TrieNode:
    def __init__(self):
        self.children = {}
        self.weight = -1
class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for index, word in enumerate(words):
            l = len(word)
            for i in range(l + 1):
                suffix = word[i:]
                key = suffix + '{' + word
                curr = self.root
                curr.weight = index
                for char in key:
                    if char not in curr.children:
                        curr.children[char] = TrieNode()
                    curr = curr.children[char]
                    curr.weight = index

    def f(self, pref: str, suff: str) -> int:
        curr = self.root
        target = suff + '{' + pref
        for char in target:
            if char not in curr.children:
                return -1
            curr = curr.children[char]
        return curr.weight


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)