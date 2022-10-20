#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for each in ops:
            if each == 'C':
                res.pop()
            elif each == 'D':
                res.append(res[-1] * 2)
            elif each == '+':
                res.append(res[-1] + res[-2])
            else:
                res.append(int(each))
        return sum(res)
# @lc code=end

