#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        p, q = n1 - 1, n2 - 1
        d1, d2 = 0, 0
        while p >= 0 or q >= 0:
            a = ' ' if p < 0 else s[p]
            b = ' ' if q < 0 else t[q]
            if a == '#':
                p -= 1
                d1 += 1
                continue
            elif b == '#':
                q -= 1
                d2 += 1
                continue
            else:
                if d1:
                    p -= 1
                    d1 -= 1
                    continue
                if d2:
                    q -= 1
                    d2 -= 1
                    continue
                if a != b:
                    return False
                else:
                    p -= 1
                    q -= 1
        return True
        
# @lc code=end

