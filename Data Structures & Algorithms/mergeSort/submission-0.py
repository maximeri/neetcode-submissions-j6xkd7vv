from typing import List

# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return f"({self.key}, \"{self.value}\")"

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # base case: 長度 <= 1，直接回傳
        if len(pairs) <= 1:
            return pairs
        
        # 找中間點
        mid = len(pairs) // 2
        
        # 遞迴排序左右半邊
        left = self.mergeSort(pairs[:mid])
        right = self.mergeSort(pairs[mid:])
        
        # 合併
        return self.merge(left, right)
    
    def merge(self, L: List[Pair], R: List[Pair]) -> List[Pair]:
        result = []
        i = j = 0
        
        # 逐一比較
        while i < len(L) and j < len(R):
            if L[i].key < R[j].key:
                result.append(L[i])
                i += 1
            elif L[i].key > R[j].key:
                result.append(R[j])
                j += 1
            else:
                # key 相等 → 選左邊，確保穩定性
                result.append(L[i])
                i += 1
        
        # 把剩下的補上
        result.extend(L[i:])
        result.extend(R[j:])
        
        return result
