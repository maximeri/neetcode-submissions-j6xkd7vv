class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, curNums, curSum):
            if curSum == target:
                res.append(curNums.copy())
                return
            if curSum > target or i == len(candidates):
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue

                # includate candidates[j]
                curNums.append(candidates[j])
                dfs(j+1, curNums, curSum + candidates[j])
                # skip candidates[j]
                curNums.pop()


        dfs(0, [], 0)
        return res