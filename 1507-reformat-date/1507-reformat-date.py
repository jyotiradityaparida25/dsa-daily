class Solution:
    def reformatDate(self, date: str) -> str:
        d={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
        l=date.split()
        r=""
        r+=l[-1]
        temp=l[0]
        
        for k,v in d.items():
            if l[-2]==k:
                r+='-'+v
        r+='-'
        day = ''.join(ch for ch in temp if ch.isdigit())
        r += day.zfill(2)
        return r
