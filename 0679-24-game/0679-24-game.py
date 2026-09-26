class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        def solve(nums: list[float]) -> bool:
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < 1e-6

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        
                        a, b = nums[i], nums[j]
                        candidates = [a + b, a - b, a * b]
                        if abs(b) > 1e-6:
                            candidates.append(a / b)

                        for val in candidates:
                            next_nums.append(val)
                            if solve(next_nums):
                                return True
                            next_nums.pop()

            return False

        return solve([float(c) for c in cards])