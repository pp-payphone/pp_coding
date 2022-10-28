#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.setdefault(n, 0) + 1
        d2 = {0: 0}
        for i in range(1, 101):
            d2[i] = d2[i - 1] + d.setdefault(i - 1, 0)
        for i, n in enumerate(nums):
            nums[i] = d2[n]
        return nums
# @lc code=end

