class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l1=s.split()
        l=[int(c) for c in l1 if c.isdigit()]
        for i in range(1,len(l)):
            if l[i]<l[i-1] or l[i]==l[i-1]:
                return False
        return True
        