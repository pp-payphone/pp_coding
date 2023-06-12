#
# @lc app=leetcode.cn id=1351 lang=python3
#
# [1351] 统计有序矩阵中的负数
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for rows in grid:
            for each in rows:
                if each < 0:
                    res += 1
        return res
# @lc code=end

