class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        sol = -1
        num = 0
        while sol < x:
            sol = num*num
            if sol == x:
                return num
            elif sol > x:
                return num-1
            num += 1
        
        

        
        
