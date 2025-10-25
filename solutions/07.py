class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        str1 = str(x)
        str2 = str1[::-1]
        y = int(str2) * sign
        if y < -2**31 or y > 2**31 - 1:
            return 0
        return y
