class Solution:
    def countSeniors(self, details: List[str]) -> int:
        l=[]
        r=""
        c=0
        for word in details:
            r+=word[len(word)-4]
            r+=word[len(word)-3]
            l.append(int(r))
            r=""
        for i in l:
            if i>60:
                c+=1
        return c
