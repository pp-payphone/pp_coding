#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        c = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                c += 1
            else:
                res = max(res, c)
                c = 1
        return max(res, c)
# @lc code=end

