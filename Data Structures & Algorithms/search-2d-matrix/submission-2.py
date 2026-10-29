class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for r in matrix:
            for num in r:
                if num == target:
                    return True

        return False

