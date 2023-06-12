#
# @lc app=leetcode.cn id=1413 lang=python3
#
# [1413] 逐步求和得到正数的最小值
#

# @lc code=start
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s = 0
        res = 1
        for n in nums:
            s += n
            res = max(res, 1 - s)
        return res
# @lc code=end

