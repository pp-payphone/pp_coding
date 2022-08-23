#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        res = []
        n = 1
        while True:
            power_n = n * n
            if power_n > 2 ** 31:
                break
            res.append(power_n)
            n += 1
        return num in res
# @lc code=end

