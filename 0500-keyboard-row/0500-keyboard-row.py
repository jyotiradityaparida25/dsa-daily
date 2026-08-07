class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l1=set("qwertyuiop")
        l2=set("asdfghjkl")
        l3=set("zxcvbnm")
        res=[]
        for word in words:
            ws=set(word.lower())
            if ws<=l1 or ws<=l2 or ws<=l3:
                res.append(word)
        return res