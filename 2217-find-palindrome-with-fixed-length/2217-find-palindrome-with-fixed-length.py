class Solution(object):
    def kthPalindrome(self, queries, intLength):
        """
        :type queries: List[int]
        :type intLength: int
        :rtype: List[int]
        """
        half = (intLength + 1) // 2
        start = 10 ** (half - 1)   
        end = 10 ** half - 1      
    
        answer = []
        for k in queries:
            prefix_num = start + k - 1
            if prefix_num > end:
                answer.append(-1)
                continue
        
            prefix = str(prefix_num)
            if intLength % 2 == 0:
                palindrome = prefix + prefix[::-1]
            else:
                palindrome = prefix + prefix[-2::-1]
        
            answer.append(int(palindrome))
    
        return answer
        