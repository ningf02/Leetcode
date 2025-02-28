#https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            chars = [s[i] for s in strs]
            if len(set(chars)) > 1:
                return shortest[0:i]
        return shortest
            
