#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    # 双指针遍历的思路是很直接的
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        p, q = 0, 0
        for q in range(n):
            if p == m:
                break
            if s[p] == t[q]:
                p += 1
        return True if p == m else False
# @lc code=end

