#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix):
        """
        思路：模拟移动路线，辅助矩阵标记是否走过这个点；可以利用原本的空间来保存是否走过的信息
        时间复杂度：O(mn)
        空间复杂度：O(1)
        """
        m = len(matrix[0])
        n = len(matrix)
        if m == 1 and n == 1:
            return [matrix[0][0]]
        res = []
        x, y = 0, 0
        count = 0
        def change_direction(direction):
            if direction == (0, 1):
                return 1, 0
            elif direction == (1, 0):
                return 0, -1
            elif direction == (0, -1):
                return -1, 0
            elif direction == (-1, 0):
                return 0, 1

        direction = (0, 1)
        while count < n*m:
            res.append(matrix[x][y])
            count += 1
            matrix[x][y] = None
            if x+direction[0] >= n or x+direction[0] < 0 or y + direction[1] >= m or y + direction[1] < 0:
                direction = change_direction(direction)
            elif matrix[x+direction[0]][y+direction[1]] is None:
                direction = change_direction(direction)
            x += direction[0]
            y += direction[1]
        return res

        
# @lc code=end

s = Solution()
res = s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
res