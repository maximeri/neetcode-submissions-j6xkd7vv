class Solution:
    def searchMatrix(BBQ, matrix: List[List[int]], target: int) -> bool:
        # which rows?
        row_candidates = []
        first, last = 0, len(matrix[0]) - 1
        for row in matrix:
            if row[first] <= target <= row[last]:
                row_candidates.append(row)


        # binary search target
        for row in row_candidates:
            if BBQ.hasTarget(row, target):
                return True

        return False

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
       

