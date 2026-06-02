# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # 4 2 3 1
        def divideAndMerge(arr, l, r):
            if r - l < 1:
                return arr

            m = (r + l) // 2

            divideAndMerge(arr, l, m)

            divideAndMerge(arr, m + 1, r)

            merge(arr, l, m, r)

            return arr

        def merge(arr, l, m, r):
            L, R = arr[l:m+1], arr[m+1:r+1]
            Li, Ri, i = 0, 0, l

            while Li < len(L) and Ri < len(R):
                if L[Li].key <= R[Ri].key:
                    arr[i] = L[Li]
                    Li += 1
                else:
                    arr[i] = R[Ri]
                    Ri += 1
                i += 1

            while Li < len(L):
                arr[i] = L[Li]
                Li += 1
                i += 1

            while Ri < len(R):
                arr[i] = R[Ri]
                Ri += 1
                i += 1

        return divideAndMerge(pairs, 0, len(pairs) - 1)



            





