class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(pattern)!=len(words):
            return False
        c2w={}
        w2c={}
        for char,word in zip(pattern,words):
            if char in c2w and c2w[char]!=word:
                return False
            if word in w2c and w2c[word]!=char:
                return False
            c2w[char]=word
            w2c[word]=char
        return True