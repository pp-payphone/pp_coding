#
# @lc app=leetcode.cn id=1260 lang=python3
#
# [1260] 二维网格迁移
#

# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            j_ = (j + k) % n
            diff = (j + k) // n
            for i in range(m):
                res[i][j_] = grid[(i - diff) % m][j]
        return res
# @lc code=end

