class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, candidateList, total):
            if total == target:
                res.append(candidateList.copy())
                return
            if total > target:
                return
            for curIndex in range(i, len(candidates)):
                if curIndex > i and candidates[curIndex] == candidates[curIndex - 1]:
                    continue
                candidateList.append(candidates[curIndex])
                dfs(curIndex + 1, candidateList, total + candidates[curIndex])
                candidateList.pop() # 這條路已經走完，不管成功或失敗，回到上個決策點

        dfs(0,[],0)
        return res
