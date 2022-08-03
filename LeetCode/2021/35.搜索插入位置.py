#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        思路：二分法查找，左边的数小于，当位子的数大于等于
        时间复杂度：O(logn)
        空间复杂度：O(1)
        """
        n = len(nums)
        left = 0
        right = n-1
        if n == 0:
            return 0
        elif nums[right] < target:
            return n
        elif nums[left] > target:
            return 0
        while left < right-1:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid
            elif target < nums[mid]:
                right = mid
            else:
                return mid
        if nums[left] == target:
            return left
        else:
            return right
        
# @lc code=end

