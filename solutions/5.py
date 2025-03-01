#https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        def expand_from_centre(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]
        longest = ""
        for i in range(len(s)):
            odd_palindrome = expand_from_centre(i, i)
            even_palindrome = expand_from_centre(i, i + 1)
            longest = max(longest, odd_palindrome, even_palindrome, key=len)
        return longest
