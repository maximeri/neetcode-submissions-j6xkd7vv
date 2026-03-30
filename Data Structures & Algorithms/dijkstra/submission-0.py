class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i: [] for i in range(n)}

        for u, v, w in edges:
            adj[u].append([v, w])

        shortest = {}
        minHeap = [[0, src]]
        while minHeap:
            curW, curN = heapq.heappop(minHeap)
            if curN in shortest:
                continue
            shortest[curN] = curW

            for neiN, neiW in adj[curN]:
                if neiN not in shortest:
                    heapq.heappush(minHeap, [curW + neiW, neiN])
            
        # Fill in missing nodes
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest




