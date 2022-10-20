#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#

# @lc code=start
class Solution:
    # 思路：遍历并计算每一个三角形的面积，时间复杂度 O(n^3)
    def largestTriangleArea(self, points) -> float:
        n = len(points)
        res = 0

        def cal_area(x, y, z):
            if x[0] > y[0]:
                x, y = y, x
            if x[0] > z[0]:
                x, z = z, x
            if y[0] > z[0]:
                y, z = z, y
            w = z[0] - x[0]
            if w == 0:
                return 0
            elif z[1] == x[1]:
                return w * abs(y[1] - z[1]) / 2
            else:
                y_ = (z[1] - x[1]) / w * (y[0] - x[0]) + x[1]
                return w * abs(y[1] - y_) / 2

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    x, y, z = points[i], points[j], points[k]
                    area = cal_area(x, y, z)
                    res = max(res, area)
        return res
# @lc code=end

Solution().largestTriangleArea([[4,6],[6,5],[3,1]])