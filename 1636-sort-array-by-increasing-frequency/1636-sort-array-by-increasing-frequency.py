class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d={}
        l=[]
        for num in nums:
            if num not in d:
                d[num]=1
            else:
                d[num]+=1
        sd=dict(sorted(d.items(),key=lambda item:(item[1], -item[0])))
        for k,v in sd.items():
            for i in range(v):
                l.append(k)
        
        return l
