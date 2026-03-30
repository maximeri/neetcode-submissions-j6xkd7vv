class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # brute force
        project_list = sorted(zip(capital, profits))
        n = len(project_list) 
        used = [False] * n

        for _ in range(k):
            best_profit = 0
            best_idx = -1
            for i in range(n):
                if project_list[i][0] > w:
                    break
                if not used[i] and project_list[i][1] > best_profit:
                    best_profit = project_list[i][1]
                    best_idx = i
            
            if best_idx == -1:
                break
            w += best_profit
            used[best_idx] = True

        return w
