#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    # 相减
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_res = (n + 1) * n / 2
        # for n in nums:
        #     sum_res -= n
        sum_res -= sum(nums)
        return int(sum_res)
# @lc code=end

