class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        labels = defaultdict(int)

        for num in nums:
            labels[num] += 1 # num : frq

        buckets = [[] for i in range(len(nums) + 1)]

        for num in labels:
            frq = labels[num]
            buckets[frq].append(num)

        res = []
        for i in range(len(buckets), 0, -1):
            for num in buckets[i - 1]:
                res.append(num)
                if len(res) == k:
                    return res
            

        

