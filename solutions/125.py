#https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.translate(str.maketrans("","",string.punctuation + " "))
        return s == s[::-1]

        
