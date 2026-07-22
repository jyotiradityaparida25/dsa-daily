class Solution:
    def partition(self, s: str) -> List[List[str]]:
        r=[]
        p=[]
        n=len(s)
        def isPalindrome(sub:str)->bool:
            return sub==sub[::-1]
        def backtrack(start:int):
            if start==n:
                r.append(p[:])
                return
            for end in range(start+1,n+1):
                substr=s[start:end]
                if isPalindrome(substr):
                    p.append(substr)
                    backtrack(end)
                    p.pop()
        backtrack(0)
        return r
        