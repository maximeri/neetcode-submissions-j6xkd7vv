# Hsuan Hsuan
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initial thought:
        # first approach (fails O(1) space): 
        #   use map with key: value -> targte - numbers[index1]: index1
        #   iterate through to see if key == numbers[index2]
        #   if matches returns
        # second approach with two pointers:
        #   need to utilize the sorted condition
        #   start from left and right most of array
        #   compare numbers[l] + numbers[r] to target
            # equal then return
            # larger then r--
            # smaller then l++
        
        # aftering reading solution:
        l, r = 0, len(numbers) - 1
        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum == target:
                return [l+1, r+1]
            if currSum < target:
                l += 1
            if currSum > target:
                r -= 1

        return []
             
    
