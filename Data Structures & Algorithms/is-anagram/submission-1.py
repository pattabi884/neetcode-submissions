class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quick check: if lengths aren't equal, they can't be anagrams
        if len(s) != len(t):
            return False
            
        count = {}
        
        # Count up for string s
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # Count down for string t
        for char in t:
            count[char] = count.get(char, 0) - 1
            
        # If any count is not 0, it's not an anagram
        for c in count.values():
            if c != 0:
                return False
                
        return True