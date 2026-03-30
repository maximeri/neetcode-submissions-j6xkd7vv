class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combs, curComb = [], []
        candidates.sort()
        def helper(i, target):
            if target == 0:
                combs.append(curComb.copy())
                return

            for j in range(i, len(candidates)):
                if candidates[j] > target:
                    break
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                curComb.append(candidates[j])
                helper(j+1, target - candidates[j])
                curComb.pop()

        helper(0, target)

        return combs