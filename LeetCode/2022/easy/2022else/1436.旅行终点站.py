#
# @lc app=leetcode.cn id=1436 lang=python3
#
# [1436] 旅行终点站
#

# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set()
        end = set()
        for s, e in paths:
            start.add(s)
            if s in end:
                end.remove(s)
            if e not in start:
                end.add(e)
        return list(end)[0]
# @lc code=end

