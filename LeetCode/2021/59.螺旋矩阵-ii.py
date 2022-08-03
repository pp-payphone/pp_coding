#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int):
        """
        思路：模拟+转向
        时间复杂度：O(n^2)
        空间复杂度：O(1)
        """
        def changederection(direction):
            x, y = direction
            if x == 0 and y == 1:
                return 1, 0
            elif x == 1 and y == 0:
                return 0, -1
            elif x == 0 and y == -1:
                return -1, 0
            else:
                return 0, 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        direction = [0, 1]
        x, y = 0, 0
        for i in range(n*n):
            res[x][y] = i+1
            if x + direction[0] >= n or x + direction[0] < 0:
                direction = changederection(direction)
            elif y + direction[1] >=n or y + direction[1] < 0:
                direction = changederection(direction)
            elif res[x+direction[0]][y+direction[1]] != 0:
                direction = changederection(direction)
            x += direction[0]
            y += direction[1]
        return res
# @lc code=end

s = Solution()
res = s.generateMatrix(3)
res