import collections

class Solution:
    def scoreOfStudents(self, s: str, answers: list[int]) -> int:
        correct_ans = eval(s)
        
        n_digits = (len(s) + 1) // 2
        dp = [[set() for _ in range(n_digits)] for _ in range(n_digits)]
        
        for i in range(n_digits):
            dp[i][i].add(int(s[i * 2]))
            
        for length in range(2, n_digits + 1):
            for i in range(n_digits - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    op = s[k * 2 + 1]
                    for left in dp[i][k]:
                        for right in dp[k + 1][j]:
                            if op == '+':
                                val = left + right
                            else:
                                val = left * right
                            if val <= 1000:
                                dp[i][j].add(val)
                                
        incorrect_valid_answers = dp[0][n_digits - 1]
        
        counts = collections.Counter(answers)
        total_points = 0
        
        for ans, count in counts.items():
            if ans == correct_ans:
                total_points += 5 * count
            elif ans in incorrect_valid_answers:
                total_points += 2 * count
                
        return total_points