#https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        output_dist = float('inf')
        output_sum = 0
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) -1 
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if output_dist > abs(total - target):
                        output_dist = abs(total - target)
                        output_sum = total
                if total > target:
                    k -= 1
                else:
                    j += 1
        return output_sum
