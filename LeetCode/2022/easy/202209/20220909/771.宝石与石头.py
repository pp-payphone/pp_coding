#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = {}
        for each in jewels:
            d[each] = True
        res = 0
        for each in stones:
            if d.get(each):
                res += 1
        return res
# @lc code=end

