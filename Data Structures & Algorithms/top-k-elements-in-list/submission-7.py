class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frq = defaultdict(int)

        for num in nums:
            frq[num] += 1

        # 1: 2 times, 3: 4 times

        res = []
        while k > 0:
            maxNum = max(frq, key=frq.get)
            # frq.pop(maxNum)
            del frq[maxNum]
            res.append(maxNum)
            k -= 1

        return res
            

