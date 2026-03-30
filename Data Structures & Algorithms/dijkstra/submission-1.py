class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i: [] for i in range(n)}

        for u, v, w in edges:
            adj[u].append((w, v))

        shortest = {}
        minHeap = []
        minHeap.append((0, src))
        while minHeap:
            curW, curN = heapq.heappop(minHeap)
            if curN in shortest:
                continue
            shortest[curN] = curW

            for neiW, neiN in adj[curN]:
                if neiN in shortest:
                    continue
                heapq.heappush(minHeap, (curW + neiW, neiN))

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest
