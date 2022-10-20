#
# @lc app=leetcode.cn id=830 lang=python3
#
# [830] 较大分组的位置
#

# @lc code=start
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        n = len(s)
        if n < 3:
            return res
        x = 0
        for y in range(1, n):
            if s[y] != s[y-1]:
                if y - 1 - x >= 2:
                    res.append([x, y - 1])
                x = y
        if y - x >= 2:
            res.append([x, y])
            x = y
        return res
# @lc code=end

