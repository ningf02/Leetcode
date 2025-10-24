class Solution:
    def checkRecord(self, s: str) -> bool:
        aCount = 0
        lCount = 0
        for i in s:
            if i == 'L':
                lCount += 1
                if lCount == 3:
                    return False
            else:
                lCount = 0
            if i == 'A':
                aCount += 1
                if aCount == 2:
                    return False
        return True
