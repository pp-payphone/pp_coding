#
# @lc app=leetcode.cn id=575 lang=python3
#
# [575] 分糖果
#

# @lc code=start
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        m = len(set(candyType))
        return min(n // 2, m)
# @lc code=end

