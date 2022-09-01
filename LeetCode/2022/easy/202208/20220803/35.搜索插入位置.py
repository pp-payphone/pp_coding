#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    # 二分查找，左边要小于它，当前要大于等于它 O(logn) O(1)
    def searchInsert(self, nums, target) -> int:
        n = len(nums)
        if nums[-1] < target:
            return n
        elif nums[0] >= target:
            return 0
        p = 0
        q = n-1
        while q - p > 1:
            mid_l = (p + q) // 2
            if nums[mid_l] < target:
                p = mid_l
            else:
                q = mid_l
        return q
# @lc code=end

Solution().searchInsert([1,3,5,6], 5)