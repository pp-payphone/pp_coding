#
# @lc app=leetcode.cn id=1523 lang=python3
#
# [1523] 在区间范围内统计奇数数目
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = (high - low) // 2
        if high % 2 == 1 or (low % 2 == 1):
            res += 1
        return res
# @lc code=end

