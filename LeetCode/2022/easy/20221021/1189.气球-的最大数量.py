#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] “气球” 的最大数量
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for s in text:
            c = d.get(s)
            if c is not None:
                d[s] = c + 1
        print(d)
        return min(d['b'], d['a'], d['l'] // 2, d['o'] // 2, d['n'])
# @lc code=end

