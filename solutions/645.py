class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        dup = -1
        for n in nums:
            if n in seen:
                dup = n
            seen.add(n)
        
        for n in range(1,len(nums)+1):
            if n not in seen:
                return [dup,n]

