class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1=nums[:n]
        l2=nums[n:]
        a,b=0,0
        l=[]
        while a<len(l1) and b<len(l2):
            l.append(l1[a])
            l.append(l2[b])
            a+=1
            b+=1
        return l