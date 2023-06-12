#
# @lc app=leetcode.cn id=1422 lang=python3
#
# [1422] 分割字符串的最大得分
#

# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        n0, n1 = 0, 0
        for each in s:
            if each == '0':
                n0 += 1
            else:
                n1 += 1
        res = 0
        left_0 = 0
        left_1 = 0
        for i in range(n - 1):
            if s[i] == '0':
                left_0 += 1
            else:
                left_1 += 1
            score = left_0 + n1 - left_1
            res = max(res, score)
        return res

# @lc code=end

