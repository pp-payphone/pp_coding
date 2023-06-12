#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = d.setdefault(num, 0) + 1
        res = 0
        for v in d.values():
            res += int(v * (v - 1) / 2)
        return res
# @lc code=end

