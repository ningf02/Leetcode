class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        lib = "aeiouAEIOU"
        vowels = []
        for i in range(len(s)):
            if s[i] in lib:
                vowels.append([i,s[i]])
        
        left = 0
        right = len(vowels) - 1
        while left < right:
            s[vowels[left][0]] = vowels[right][1]
            s[vowels[right][0]] = vowels[left][1]
            left += 1
            right -= 1
        return ''.join(s)
       
