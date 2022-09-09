#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums) -> int:
        n = len(nums)
        s = sum(nums)
        if s - nums[0] == 0:
            return 0
        left_sum = 0
        right_sum = s - nums[0]

        for i in range(1, n):
            left_sum += nums[i - 1]
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
        return -1
# @lc code=end

Solution().pivotIndex([1,7,3,6,5,6])