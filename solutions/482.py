class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-','').upper()
        remainder = len(s) % k
        groups = []
        if remainder:
            groups.append(s[:remainder])
        for i in range(remainder, len(s), k):
            groups.append(s[i:i+k])
        return '-'.join(groups)
        
        
        
