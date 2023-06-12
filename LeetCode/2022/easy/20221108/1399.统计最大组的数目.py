#
# @lc app=leetcode.cn id=1399 lang=python3
#
# [1399] 统计最大组的数目
#

# @lc code=start
class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = {}
        for i in range(1, n + 1):
            c = 0
            while i:
                c += i % 10
                i //= 10
            d[c] = d.setdefault(c, 0) + 1
        max_c = max(d.values())
        res = 0
        for c in d.values():
            if c == max_c:
                res += 1
        return res
# @lc code=end

