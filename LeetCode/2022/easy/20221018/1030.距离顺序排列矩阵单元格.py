#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#

# @lc code=start
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        maxDist = max(rCenter, rows - 1 - rCenter) + max(cCenter, cols - 1 - cCenter)
        row, col = rCenter, cCenter
        ret = [[row, col]]
        for dist in range(1, maxDist + 1):
            row -= 1
            for i, (dr, dc) in enumerate(dirs):
                while (i % 2 == 0 and row != rCenter) or (i % 2 != 0 and col != cCenter):
                    if 0 <= row < rows and 0 <= col < cols:
                        ret.append([row, col])
                    row += dr
                    col += dc
        return ret

# @lc code=end

