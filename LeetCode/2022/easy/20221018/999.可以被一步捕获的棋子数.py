#
# @lc app=leetcode.cn id=999 lang=python3
#
# [999] 可以被一步捕获的棋子数
#

# @lc code=start
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        f = False
        for x in range(8):
            for y in range(8):
                if board[x][y] == 'R':
                    f = True
                    break
            if f:
                break
        res = 0
        for i in range(x - 1, -1, -1):
            v = board[i][y]
            if v == 'B':
                break
            elif v == 'p':
                res += 1
                break
        for i in range(x + 1, 8):
            v = board[i][y]
            if v == 'B':
                break
            elif v == 'p':
                res += 1
                break

        for j in range(y - 1, -1, -1):
            v = board[x][j]
            if v == 'B':
                break
            elif v == 'p':
                res += 1
                break
        for j in range(y + 1, 8):
            v = board[x][j]
            if v == 'B':
                break
            elif v == 'p':
                res += 1
                break

        return res
# @lc code=end

