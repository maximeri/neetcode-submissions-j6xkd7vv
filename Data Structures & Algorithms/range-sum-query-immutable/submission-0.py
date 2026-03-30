class NumArray:
    def __init__(self, nums: List[int]):
        self.p = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.p[i+1] = self.p[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.p[right + 1] - self.p[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)