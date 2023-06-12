#
# @lc app=leetcode.cn id=1518 lang=python3
#
# [1518] 换水问题
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        Bottles = numBottles
        while Bottles >= numExchange:
            res += Bottles // numExchange
            Bottles = Bottles // numExchange + Bottles % numExchange
        return res

# @lc code=end

