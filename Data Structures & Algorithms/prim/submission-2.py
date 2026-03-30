class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        minHeap = [(0, 0)]
        visited = set()
        res = 0

        while minHeap and len(visited) < n:
            curW, curN = heapq.heappop(minHeap)
            if curN in visited:
                continue
            res += curW
            visited.add(curN)

            for neiN, neiW in adj[curN]:
                if neiN not in visited:
                    heapq.heappush(minHeap, (neiW, neiN))

        for i in range(n):
            if i not in visited:
                return -1

        return res
                

