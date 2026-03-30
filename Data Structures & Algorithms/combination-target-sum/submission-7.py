class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs, curComb = [], []

        def helper(i, curTarget):
            if curTarget == 0:
                combs.append(curComb.copy())
                return
            
            for j in range(i, len(nums)):
                if curTarget < 0:
                    return
                curComb.append(nums[j])
                # 直接在呼叫函式時「傳入計算結果」。這樣『不會改變當前層的 curTarget 數值』，也就不需要手動加回來
                helper(j, curTarget - nums[j])
                curComb.pop()

        helper(0, target)

        return combs