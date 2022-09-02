#
# @lc app=leetcode.cn id=598 lang=python3
#
# [598] 范围求和 II
#

# @lc code=start
class Solution:
    # 思路： 0,0位置的一定是最大整数
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # if ops == []:
        #     return m * n
        min_x, min_y = m, n
        for x, y in ops:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
        return min_x * min_y
# @lc code=end

