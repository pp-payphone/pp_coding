#
# @lc app=leetcode.cn id=1380 lang=python3
#
# [1380] 矩阵中的幸运数
#

# @lc code=start
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        rowmax_dict = {}
        for i in range(m):
            max_num = 10 ** 6
            for j in range(n):
                if max_num > matrix[i][j]:
                    max_idx = j
                    max_num = min(max_num, matrix[i][j])
            rowmax_dict[i] = max_idx
        colmin_dict = {}
        for j in range(n):
            min_num = 0
            for i in range(m):
                if min_num < matrix[i][j]:
                    min_idx = i
                    min_num = max(min_num, matrix[i][j])
            colmin_dict[j] = min_idx
        res = []
        for i in range(m):
            j = rowmax_dict[i]
            if colmin_dict[j] == i:
                res.append(matrix[i][j])
        return res
# @lc code=end

