#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack.find(needle) != -1:
            return haystack.find(needle)
        else:
             return -1
