#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = {}
        for e in s:
            m[e] = m.setdefault(e, 0) + 1
        f = False
        res = 0
        for v in m.values():
            if v % 2 == 1:
                f = True
            res += (v // 2) * 2
        if f:
            res += 1
        return res
# @lc code=end

