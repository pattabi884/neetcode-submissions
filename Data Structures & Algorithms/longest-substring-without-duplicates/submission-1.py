class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        longest = 0 
        for right in range(len(s)):
            while s[right] in seen:
                del seen[s[left]]
                left += 1
                
            seen[s[right]] = True
            current = right - left + 1
            longest = max(current, longest)
        return longest 
