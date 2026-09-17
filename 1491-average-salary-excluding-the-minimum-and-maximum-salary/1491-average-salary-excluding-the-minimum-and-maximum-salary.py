class Solution:
    def average(self, salary: list[int]) -> float:
        total_sum = sum(salary)
        min_salary = min(salary)
        max_salary = max(salary)
        
        return (total_sum - min_salary - max_salary) / (len(salary) - 2)