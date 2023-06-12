#
# @lc app=leetcode.cn id=1217 lang=python3
#
# [1217] 玩筹码
#

# @lc code=start
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        cnt1, cnt2 = 0, 0
        for n in position:
            if n % 2 == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        return min(cnt1, cnt2)
# @lc code=end

