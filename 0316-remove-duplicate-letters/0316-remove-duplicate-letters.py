class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lc={c:i for i,c  in enumerate(s) }
        st=[]
        in_s=set()
        for i,c in enumerate(s):
            if c in in_s:
                continue
            while st and st[-1] >c and lc[st[-1]]>i:
                in_s.remove(st.pop())
            st.append(c)
            in_s.add(c)
        return "".join(st)