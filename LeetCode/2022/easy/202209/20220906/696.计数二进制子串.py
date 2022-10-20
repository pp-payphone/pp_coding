#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0
        res = 0
        a, b = 0, 1
        for i in range(1, n):
            if s[i] == s [i - 1]:
                b += 1
            else:
                res += min(a, b)
                a, b = b, 1
        res += min(a, b)
        return res
# @lc code=end

