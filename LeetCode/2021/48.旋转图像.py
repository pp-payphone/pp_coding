#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        思路：分层四个交换值
            1.2-3-->1;4-5-->6
        时间复杂度：O(n^2)
        空间复杂度：O(1)
        """
        n = len(matrix)
        if n == 1:
            return
        for i in range(n//2):
            for j in range(i, n-1-i):
                t = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][0+i]
                matrix[n-1-j][0+i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[0+j][n-1-i]
                matrix[0+j][n-1-i] = t
        return
        
# @lc code=end

