class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        res=''
        for w in words:
            res+=w
            if res==s:
                return True
        return False