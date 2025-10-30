class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        d = {}
        for char, word in zip(pattern, words):
            if char in d:
                if word != d[char]:
                    return False
            else:
                if word in d.values():
                    return False
            d[char] = word
        return True
        
