class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrq = defaultdict(int)

        for n in nums:
            numFrq[n] += 1

        # 1: 1, 2: 2

        buckets = [[] for _ in range(len(nums) + 1)]

        for (num, frq) in numFrq.items():
            buckets[frq].append(num)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            bucket = buckets[i]
            for j in range(len(bucket) - 1, -1, -1):
                res.append(bucket[j])
                if len(res) == k:
                    return res
