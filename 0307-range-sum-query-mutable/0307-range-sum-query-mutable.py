class NumArray:
    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.nums = nums
        self.bit = [0] * (self.n + 1)
        for i in range(self.n):
            self._add(i, nums[i])

    def _add(self, index: int, delta: int) -> None:
        i = index + 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & (-i)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index, delta)

    def _query(self, index: int) -> int:
        s = 0
        i = index + 1
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s

    def sumRange(self, left: int, right: int) -> int:
        return self._query(right) - self._query(left - 1)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)