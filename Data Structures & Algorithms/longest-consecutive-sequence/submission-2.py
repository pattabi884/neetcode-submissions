class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        
        numSet = set(nums)
        for num in numSet:
            if num - 1 not in numSet:
                current = 1
                while num + 1 in numSet:
                
                    current += 1
                    
                    num += 1
                longest = max(longest, current)
        return longest