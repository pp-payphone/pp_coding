#
# @lc app=leetcode.cn id=1275 lang=python3
#
# [1275] 找出井字棋的获胜者
#

# @lc code=start
class Solution:
    def tictactoe(self, moves) -> str:
        grid = [[0 for _ in range(3)] for _ in range(3)]
        v = 1
        for i, j in moves:
            grid[i][j] = v
            v *= -1
        for i in range(3):
            if grid[i][0] + grid[i][1] + grid[i][2] == 3:
                return 'A'
            elif grid[i][0] + grid[i][1] + grid[i][2] == -3:
                return 'B'
        for j in range(3):
            if grid[0][j] + grid[1][j] + grid[2][j] == 3:
                return 'A'
            elif grid[0][j] + grid[1][j] + grid[2][j] == -3:
                return 'B'
        if grid[0][0] + grid[1][1] + grid[2][2] == 3:
            return 'A'
        elif grid[0][0] + grid[1][1] + grid[2][2] == -3:
            return 'B'
        if grid[2][0] + grid[1][1] + grid[0][2] == 3:
            return 'A'
        elif grid[2][0] + grid[1][1] + grid[0][2] == -3:
            return 'B'
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    return 'Pending'
        return 'Draw'
# @lc code=end
Solution().tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]])
