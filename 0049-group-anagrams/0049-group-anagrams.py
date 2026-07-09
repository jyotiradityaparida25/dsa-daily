from collections import defaultdict
#from typing import List
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        am=defaultdict(list)
        for i in strs:
            s="".join(sorted(i))
            am[s].append(i)
        return list(am.values())
        