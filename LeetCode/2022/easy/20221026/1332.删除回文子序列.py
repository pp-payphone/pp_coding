#
# @lc app=leetcode.cn id=1332 lang=python3
#
# [1332] 删除回文子序列
#

# @lc code=start
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # cnt = 0
        # while s:
        #     n = len(s)
        #     for i in range(n, 0, -1):
        #         s_t = s[:i]
        #         if s_t == s_t[::-1]:
        #             cnt += 1
        #             s = s[i:]
        #             break
        # return cnt

        return 1 if s == s[::-1] else 2
# @lc code=end

