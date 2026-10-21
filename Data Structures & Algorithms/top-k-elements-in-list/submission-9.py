class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        numCounts = defaultdict(int)

        for num in nums:
            numCounts[num] += 1

        sort = [[] for _ in range(n + 1)]

        for num, count in numCounts.items():
            sort[count].append(num)

        res = []
        for i in range(len(sort) - 1, -1, -1):
            sortNums = sort[i]
            for sortNum in sortNums:
                res.append(sortNum)
                if len(res) == k:
                    return res