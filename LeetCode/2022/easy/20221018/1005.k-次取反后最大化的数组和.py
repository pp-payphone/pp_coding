#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#

# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        p = 0
        for _ in range(k):
            if nums[p] >= 0:
                nums[p] = -nums[p]
            else:
                nums[p] = -nums[p]
                p += 1
                if p == n:
                    p = n - 1
                elif nums[p - 1] <= nums[p]:
                    p -= 1
        return sum(nums)
# @lc code=end

