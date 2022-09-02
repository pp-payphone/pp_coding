#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# @lc code=start
class Solution:
    # 最大的三个数，还有一正两负的情况
    def maximumProduct(self, nums: List[int]) -> int:
        a, b, c = -1001, -1001, -1001 # 最大的三个数
        x, y, z = 1001, 1001, 1001 # 最小的三个数
        for n in nums:
            if n > a:
                a, b, c = n, a, b
            elif n > b:
                b, c = n, b
            elif n > c:
                c = n

            if n < x:
                x, y, z = n, x, y
            elif n < y:
                y, z = n, y
            elif n < z:
                z = n

        return max(a * b * c, x * y * a)
# @lc code=end

