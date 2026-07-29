class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def dfs(idx, path, value, prev):
            if idx == len(num):
                if value == target:
                    res.append(path)
                return
            
            for i in range(idx, len(num)):
                if i > idx and num[idx] == '0':
                    break
                
                curr_str = num[idx:i + 1]
                curr_val = int(curr_str)
                
                if idx == 0:
                    dfs(i + 1, curr_str, curr_val, curr_val)
                else:
                    dfs(i + 1, path + '+' + curr_str, value + curr_val, curr_val)
                    dfs(i + 1, path + '-' + curr_str, value - curr_val, -curr_val)
                    dfs(i + 1, path + '*' + curr_str, value - prev + prev * curr_val, prev * curr_val)
                    
        if num:
            dfs(0, "", 0, 0)
            
        return res