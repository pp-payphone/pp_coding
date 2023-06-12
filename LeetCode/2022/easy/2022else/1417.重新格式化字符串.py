#
# @lc app=leetcode.cn id=1417 lang=python3
#
# [1417] 重新格式化字符串
#

# @lc code=start
class Solution:
    def reformat(self, s: str) -> str:
        s1, s2 = '', ''
        for each in s:
            if each in '0123456789':
                s1 += each
            else:
                s2 += each
        n1, n2 = len(s1), len(s2)
        res = ''
        if n1 - n2 in [0, 1]:
            for i, each in enumerate(s1):
                res += each
                if i < n2:
                    res += s2[i]
        elif n1 - n2 == -1:
            for i, each in enumerate(s2):
                res += each
                if i < n1:
                    res += s1[i]
        return res

# @lc code=end

