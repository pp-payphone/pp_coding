#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        n = len(s)
        s = list(s)
        p, q = 0, n - 1
        eng = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        while p < q:
            if s[p] not in eng:
                p += 1
            elif s[q] not in eng:
                q -= 1
            else:
                s[p], s[q] = s[q], s[p]
                p += 1
                q -= 1
        return ''.join(s)

# @lc code=end

