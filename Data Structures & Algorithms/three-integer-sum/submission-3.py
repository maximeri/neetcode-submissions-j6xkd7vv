class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # solution: sort first -> one fixed size + two sum
        # since it is sorted, two sum can be solved with two pointers instead of hash map
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if a > 0:
                break

            if i >= 1 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            target = -1 * a
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # if we do not skip r, since we already skipped l
                    # it will end of doing a search that end ups with no result
                    # since l is already ruled out (this is two sum r + l = target, no other element can replace l)
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

         

