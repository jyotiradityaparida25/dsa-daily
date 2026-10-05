class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        c=0
        s=set('aeiouAEIOU')
        for i in range(left,right+1):
            w=words[i]
            if w[0] in s and w[len(w)-1] in s:
                c+=1
                
        
        return c