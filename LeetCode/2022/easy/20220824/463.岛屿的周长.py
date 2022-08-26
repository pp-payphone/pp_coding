#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    # 思路：外面补一圈0（或者不补的话自己注意条件筛选），横着遍历一次，竖着遍历一次，总共时间复杂度 O(m*n)
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        # 先横向遍历
        for i in range(row):
            for j in range(col - 1):
                if grid[i][j] != grid[i][j + 1]:
                    res += 1
        # 再纵向遍历
        for j in range(col):
            for i in range(row - 1):
                if grid[i][j] != grid[i + 1][j]:
                    res += 1
        # 最后遍历四周
        for i in range(row):
            if grid[i][0] == 1:
                res += 1
            if grid[i][-1] == 1:
                res += 1
        for j in range(col):
            if grid[0][j] == 1:
                res += 1
            if grid[-1][j] == 1:
                res += 1
        return res
# @lc code=end

