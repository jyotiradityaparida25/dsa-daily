class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def check(s):
            for i in range(1,len(s)):
                if ord(s[i-1])>ord(s[i]):
                    return False
        
        l=[]
        temp=''
        c=0
        for i in range(len(strs[0])):
            temp=''
            for w in strs:
                temp+=w[i]
            l.append(temp)

        for word in l:
            if check(word)==False:
                c+=1
        
        return c
