class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        max_len = max(len(word) for word in wordDict) if wordDict else 0
        
        dp = [False] * (len(s) + 1)
        dp[0] = True  
        
        for i in range(1, len(s) + 1):
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  
                    
        return dp[len(s)]