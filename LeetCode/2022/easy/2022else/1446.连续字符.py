#
# @lc app=leetcode.cn id=1446 lang=python3
#
# [1446] 连续字符
#

# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        p, q = 0, 0
        res = 1
        for q in range(1, n):
            if s[q] != s[q - 1]:
                res = max(q - p, res)
                p = q
        res = max(q + 1 - p, res)
        return res
# @lc code=end

