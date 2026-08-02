class Solution:
    def sortVowels(self, s: str) -> str:
        l1=['a','e','i','o','u','A','E','I','O','U']
        l2=list(s)
        l3=[]
        for char in l2:
            if char in l1:
                l3.append(char)
        l3.sort()
        idx=0
        for i in range(len(l2)):
            if l2[i] in l1:
                l2[i]=l3[idx]
                idx+=1
        return "".join(l2)
