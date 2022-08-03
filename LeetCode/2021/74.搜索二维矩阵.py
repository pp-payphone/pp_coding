#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        思路：这就是个二分法
        时间复杂度：O(log(mn))
        空间复杂度：O(1)
        """
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m*n-1
        if matrix[0][0] > target:
            return False
        elif matrix[m-1][n-1] < target:
            return False
        while True:
            mid = (l + r)//2
            if matrix[mid//n][mid%n] <= target:
                l = mid
            else:
                r = mid
            if l+1 >= r:
                if matrix[l//n][l%n] == target or matrix[r//n][r%n] == target:
                    return True
                else:
                    return False

# @lc code=end

