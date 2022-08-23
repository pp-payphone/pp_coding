#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        m = len(g)
        n = len(s)
        if n == 0:
            return 0
        g.sort()
        s.sort()
        p, q = 0, 0
        res = 0
        while p < m and q < n:
            if g[p] <= s[q]:
                p += 1
                q += 1
                res += 1
            else:
                q += 1
        return res

# @lc code=end

