class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        l,r=0,len(height)-1
        lm,rm=0,0
        total=0
        while l<r:
            if height[l]<=height[r]:
                if height[l]>=lm:
                    lm=height[l]
                else:
                    total+=lm-height[l]
                l+=1
            else:
                if height[r]>=rm:
                    rm=height[r]
                else:
                    total+=rm-height[r]
                r-=1
        return total
        