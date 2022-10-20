#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#

# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        c = 0
        d = 0
        for i in range(m):
            for j in range(n):
                c1 = grid[i][j]
                if c1 > 1:
                    c += c1 - 1
                if i != m - 1:
                    c += min(c1, grid[i + 1][j])
                if j != n - 1:
                    c += min(c1, grid[i][j + 1])
                d += c1
        return d * 6 - c * 2

# @lc code=end

