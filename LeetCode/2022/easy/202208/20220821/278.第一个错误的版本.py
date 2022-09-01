#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # 二分法
    def firstBadVersion(self, n: int) -> int:
        x, y = 1, n
        assert isBadVersion(y)
        if isBadVersion(x):
            return 1
        while y - x > 1:
            mid_l = (x + y) // 2
            if isBadVersion(mid_l):
                y = mid_l
            else:
                x = mid_l
        return y
        
# @lc code=end

