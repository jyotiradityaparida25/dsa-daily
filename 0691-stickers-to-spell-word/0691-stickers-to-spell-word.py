class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        target_counts = Counter(target)
        filtered_stickers = []
        for sticker in stickers:
            s_count = Counter(sticker)
            if any(char in target_counts for char in s_count):
                filtered_stickers.append(s_count)
                
        memo = {"": 0}
        
        def dfs(remain: str) -> int:
            if remain in memo:
                return memo[remain]
                
            first_char = remain[0]
            min_stickers = float('inf')
            
            for s_count in filtered_stickers:
                if first_char not in s_count:
                    continue
                    
                rem_counts = Counter(remain)
                rem_counts.subtract(s_count)
                
                next_remain = "".join(sorted(char * count for char, count in rem_counts.items() if count > 0))
                
                res = dfs(next_remain)
                if res != -1:
                    min_stickers = min(min_stickers, 1 + res)
                    
            memo[remain] = min_stickers if min_stickers != float('inf') else -1
            return memo[remain]
            
        return dfs("".join(sorted(target)))