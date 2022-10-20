#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        if n <= 2:
            return True
        p, q = 0, n-1
        c = 0
        while p < q:
            if s[p] == s[q]:
                p += 1
                q -= 1
            elif c == 0: # 第一次出现不一致
                a, b = p, q
                p += 1
                c += 1
            elif c == 1:
                p = a
                q = b - 1
                c += 1
            else:
                return False
        return True
# @lc code=end

