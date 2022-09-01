#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        res = ''
        iters = n // k
        reverse_flag = True
        i = -1
        for i in range(iters):
            if reverse_flag:
                res += s[i * k: (i + 1) * k][::-1]
            else:
                res += s[i * k: (i + 1) * k]
            reverse_flag = not reverse_flag
        if reverse_flag:
            res += s[(i + 1) * k:][::-1]
        else:
            res += s[(i + 1) * k:]
        return res
# @lc code=end

