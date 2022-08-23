#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    # 2 -- 1
    # 2 + 3 -- 2
    # 2 + 3 + 4 -- 3
    # (2 + (2 + n - 1)) * n / 2 = n * (n + 3) / 2 = y
    def arrangeCoins(self, n: int) -> int:
        import math
        return int((-3 + math.sqrt(9 + 8 * (n - 0.0001))) / 2) + 1
# @lc code=end

