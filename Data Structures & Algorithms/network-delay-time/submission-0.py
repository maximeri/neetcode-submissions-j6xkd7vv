class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n+1)}

        for ui, vi, ti in times:
            adj[ui].append((vi, ti))

        minHeap = []
        heapq.heappush(minHeap, (0, k))
        shortest = {}

        while minHeap:
            curW, curN = heapq.heappop(minHeap)
            if curN in shortest:
                continue
            shortest[curN] = curW
            for neiN, neiW in adj[curN]:
                if neiN in shortest:
                    continue
                heapq.heappush(minHeap, (curW + neiW, neiN))


        for i in range(1, n+1):
            if i not in shortest:
                return -1

        return max(shortest.values())
