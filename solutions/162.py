
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = (left+right) // 2
                left_val = nums[mid-1] if mid > 0 else float('-inf')
                right_val = nums[mid+1] if mid < len(nums) - 1 else float('-inf')
                if nums[mid] > left_val and nums[mid] > right_val:
                    return mid
                elif nums[mid] < left_val:
                    right = mid - 1
                elif nums[mid] < right_val:
                    left = mid + 1
