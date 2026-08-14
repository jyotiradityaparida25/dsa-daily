class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))
        
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        total = sum(days_in_month[:month - 1])
        
        total += day
        
        if month > 2:
            
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                total += 1
                
        return total