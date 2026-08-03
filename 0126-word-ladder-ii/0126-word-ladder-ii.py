from collections import defaultdict
from typing import List
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
            
        layer = {beginWord}
        parents = defaultdict(list)
        found = False
        
        while layer and not found:
            word_set -= layer
            next_layer = set()
            
            for word in layer:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c != word[i]:
                            new_word = word[:i] + c + word[i+1:]
                            if new_word in word_set:
                                next_layer.add(new_word)
                                parents[new_word].append(word)
                                if new_word == endWord:
                                    found = True
            layer = next_layer
            
        res = []
        if found:
            def dfs(node, path):
                if node == beginWord:
                    res.append(path[::-1])
                    return
                for parent in parents[node]:
                    dfs(parent, path + [parent])
                    
            dfs(endWord, [endWord])
            
        return res