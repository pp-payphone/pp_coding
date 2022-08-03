#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        """
        思路：动态规划，利用地图的空间
        时间复杂度：O(mn)
        空间复杂度：O(1)
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 1:
            for j in range(n):
                if obstacleGrid[0][j] == 1:
                    return 0
            return 1
        if n == 1:
            for i in range(m):
                if obstacleGrid[i][0] == 1:
                    return 0
            return 1
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        root = 1
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                root = 0
            obstacleGrid[0][j] = root
        root = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                root = 0
            obstacleGrid[i][0] = root
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]
# @lc code=end

s = Solution()
res = s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
res