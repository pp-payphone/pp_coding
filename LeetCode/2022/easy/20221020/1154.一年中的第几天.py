#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#

# @lc code=start
class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = date.split('-')
        y, m, d = int(y), int(m), int(d)
        res = 0
        for i in range(1, m):
            if i in (1, 3, 5, 7, 8, 10, 12):
                res += 31
            elif i == 2:
                if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
                    res += 29
                else:
                    res += 28
            else:
                res += 30
        return res + d
# @lc code=end

