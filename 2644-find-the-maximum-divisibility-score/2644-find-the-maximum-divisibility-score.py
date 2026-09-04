class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        best_divisor = divisors[0]
        best_score = -1
        for d in divisors:
            sc = 0
            for num in nums:
                if num % d == 0:
                    sc += 1
            if sc > best_score or (sc == best_score and d < best_divisor):
                best_score = sc
                best_divisor = d
        return best_divisor