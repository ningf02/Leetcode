#https://leetcode.com/problems/two-sum/

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_list = {}
        for i, num in enumerate(nums):
            reminder = target - num
            if reminder in nums_list:
                return [i, nums_list[reminder]]
            nums_list[num] = i
