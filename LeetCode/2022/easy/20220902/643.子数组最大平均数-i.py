#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if k == n:
            return sum(nums) / n
        s = sum(nums[:k])
        res = s / k
        for i in range(k, n):
            s += nums[i]
            s -= nums[i - k]
            res = max(res, s / k)
        return res

# @lc code=end

