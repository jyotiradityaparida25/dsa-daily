class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st=[]
        for token in tokens:
            if token in {'+','-','*','/'}:
                b=st.pop()
                a=st.pop()
                if token=='+':
                    st.append(a+b)
                elif token=='-':
                    st.append(a-b)
                elif token=='*':
                    st.append(a*b)
                elif token=='/':
                    st.append(int(float(a)/b))
            else:
                st.append(int(token))
        return st[0]
        