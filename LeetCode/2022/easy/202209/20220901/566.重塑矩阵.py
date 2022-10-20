#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat

        res = [[0 for _ in range(c)] for _ in range(r)]
        for y in range(m * n):
            res[y // c][y % c] = mat[y // n][y % n]

        return res
# @lc code=end

