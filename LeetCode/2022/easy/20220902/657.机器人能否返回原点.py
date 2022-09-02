#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        d = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
        for s in moves:
            d[s] += 1
        return d['U'] == d['D'] and d['L'] == d['R']
# @lc code=end

