#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        思路：依旧动态规划
        时间复杂度：O(mn)
        空间复杂度：O(1)
        """
        m = len(grid)
        n = len(grid[0])
        if m == 1 or n == 1:
            res = 0
            for i in range(m):
                for j in range(n):
                    res += grid[i][j]
            return res
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]
# @lc code=end

