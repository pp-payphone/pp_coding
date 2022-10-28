#
# @lc app=leetcode.cn id=1331 lang=python3
#
# [1331] 数组序号转换
#

# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = set(arr)
        l = list(s)
        l.sort()
        d = {}
        for i, v in enumerate(l):
            d[v] = i + 1
        res = []
        for each in arr:
            res.append(d[each])
        return res
# @lc code=end

