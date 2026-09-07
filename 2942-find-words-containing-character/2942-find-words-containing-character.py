class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l=0
        li=[]
        for word in words:
            if x in word:
                li.append(l)
            l+=1
        return li