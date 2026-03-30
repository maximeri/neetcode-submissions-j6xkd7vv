class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i: [] for i in range(n)}
        
        for (a, b), prob in zip(edges, succProb):
            adj[a].append((b, prob))
            adj[b].append((a, prob))

        minHeap = []
        heapq.heappush(minHeap, (-1, start_node))
        shortest = {}

        while minHeap:
            curW, curN = heapq.heappop(minHeap)
            if curN == end_node:
                return -curW
            if curN in shortest:
                continue

            shortest[curN] = curW

            for neiN, neiW in adj[curN]:
                if neiN not in shortest:
                    heapq.heappush(minHeap, (curW * neiW, neiN))

        return 0


