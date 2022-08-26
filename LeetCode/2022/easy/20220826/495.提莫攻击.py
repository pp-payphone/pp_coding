#
# @lc app=leetcode.cn id=495 lang=python3
#
# [495] 提莫攻击
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0:
            return 0
        right = 0
        res = 0
        for t in timeSeries:
            if t > right:
                res += duration
            else:
                res += duration - (right - t)
            right = t + duration
        return res


# @lc code=end

