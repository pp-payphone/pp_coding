#
# @lc app=leetcode.cn id=1266 lang=python3
#
# [1266] 访问所有点的最小时间
#

# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        if n == 1:
            return 0
        for i in range(n - 1):
            a, b = points[i], points[i + 1]
            res += max(abs(a[0] - b[0]), abs(a[1] - b[1]))
        return res
# @lc code=end

