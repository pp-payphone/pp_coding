#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        res = 0
        while z != 0:
            z = z & (z - 1)
            res += 1
        return res
# @lc code=end

