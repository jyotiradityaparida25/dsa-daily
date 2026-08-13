class Solution:
    def defangIPaddr(self, address: str) -> str:
        l=list(address.split('.'))
        temp=''
        for i in range(len(l)-1):
            temp+=l[i]+'[.]'
        temp+=l[len(l)-1]
        return temp