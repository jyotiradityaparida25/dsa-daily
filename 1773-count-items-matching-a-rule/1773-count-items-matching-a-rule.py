class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d={'type':0,'color':1,'name':2}
        idx=d[ruleKey]
        c=0
        for item in items:
            if item[idx]==ruleValue:
                c+=1
        return c