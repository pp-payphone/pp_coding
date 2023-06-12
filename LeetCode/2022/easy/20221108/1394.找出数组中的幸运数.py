#
# @lc app=leetcode.cn id=1394 lang=python3
#
# [1394] 找出数组中的幸运数
#

# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for n in arr:
            d[n] = d.setdefault(n, 0) + 1
        res = -1
        for k, v in d.items():
            if k == v:
                res = max(res, k)
        return res
# @lc code=end

