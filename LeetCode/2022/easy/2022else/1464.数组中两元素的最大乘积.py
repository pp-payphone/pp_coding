#
# @lc app=leetcode.cn id=1464 lang=python3
#
# [1464] 数组中两元素的最大乘积
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1, m2 = 0, 0
        for each in nums:
            if each > m1:
                m1, m2 = each, m1
            elif each > m2:
                m2 = each
        return (m1 - 1) * (m2 - 1)
# @lc code=end

