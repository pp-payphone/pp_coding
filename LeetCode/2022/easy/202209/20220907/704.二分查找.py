#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        p, q = 0, n - 1
        if nums[p] > target:
            return -1
        if nums[q] < target:
            return -1
        while p < q - 1:
            mid_l = (p + q) // 2
            if nums[mid_l] <= target:
                p = mid_l
            else:
                q = mid_l
        if nums[p] == target:
            return p
        elif nums[q] == target:
            return q
        else:
            return -1

# @lc code=end

