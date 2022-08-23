#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        s_l = list(s)
        p, q = 0, n - 1
        target = 'aeiouAEIOU'
        while p < q:
            if s_l[p] in target and s_l[q] in target:
                s_l[p], s_l[q] = s_l[q], s_l[p]
                p +=1
                q -= 1
            else:
                if s_l[p] not in target:
                    p += 1
                if s_l[q] not in target:
                    q -= 1
        return ''.join(s_l)


# @lc code=end

