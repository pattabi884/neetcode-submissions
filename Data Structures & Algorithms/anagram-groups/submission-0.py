class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        res = []
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            f = tuple(freq)
            count[f] = count.get(f, []) + [word]
        for words in count.values():
            res.append(words)
        return res            
        