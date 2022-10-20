#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        map = {}
        n = len(nums)
        res = n
        d_cnts = 0
        for idx, num in enumerate(nums):
            c, x, y = map.setdefault(num, [0, idx, idx])
            c += 1
            y = idx
            map[num] = c, x, y
            if c > d_cnts:
                d_cnts = c
                res = y - x + 1
            elif c == d_cnts:
                res = min(res, y- x + 1)
        return res
# @lc code=end

