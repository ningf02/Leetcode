class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i,j = len(a)-1, len(b)-1
        carry = 0
        total = []

        while i >= 0 or j >= 0 or carry == 1:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0
            sum = x + y + carry 
            total.append(str(sum%2))
            carry = sum // 2
            i -= 1
            j -= 1
        
        return ''.join(total[::-1])       
