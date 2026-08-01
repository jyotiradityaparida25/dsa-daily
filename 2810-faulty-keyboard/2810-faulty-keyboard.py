class Solution:
    def finalString(self, s: str) -> str:
        def rev(s):
            l=len(s)
            left=0
            right=l-1
            while left<right:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            return s
        l1=list(s)
        l2=[]
        for i in range(len(l1)):
            if l1[i]!='i':
                l2.append(l1[i])
            elif l1[i]=='i':
                rev(l2)
                #l2.append(l1[i])
        return "".join(l2)