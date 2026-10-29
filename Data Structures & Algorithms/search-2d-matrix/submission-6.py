class Solution:
    def searchMatrix(BBQ, matrix: List[List[int]], target: int) -> bool:
        # which last rows

        l, r = 0, len(matrix) - 1
        rowLen = len(matrix[0])
        targetRow = False
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][rowLen - 1]:
                targetRow = matrix[m]
            
            if matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
                
        # binary search target
        return targetRow and BBQ.hasTarget(targetRow, target)
          
    def hasTarget(BBQ, arr: list, target) -> bool:
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if arr[m] == target:
                return True

            if arr[m] < target:
                l = m + 1
            else:
                r = m - 1

        return False
       

