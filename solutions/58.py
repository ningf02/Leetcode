#https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                count += 1
            else:
                break           
        return count
            

