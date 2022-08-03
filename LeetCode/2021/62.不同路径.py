#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        思路：
            1.递归+回溯(太慢了)
            2.正向递推(O(mn),O(mn)) -- 动态规划
            3.组合数学：从m+n-2步中抽取m-1次向下
        时间复杂度：
        空间复杂度：
        """
        # if m == 1 or n == 1:
        #     return 1
        # res = [[0 for _ in range(n)] for _ in range(m)]
        # for i in range(n):
        #     res[0][i] = 1
        # for j in range(m):
        #     res[j][0] = 1
        # for i in range(1, m):
        #     for j in range(1, n):
        #         res[i][j] = res[i-1][j] + res[i][j-1]
        # return res[m-1][n-1]
        return comb(m + n - 2, n - 1)

# @lc code=end

