#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p, q = 0, 1
        while p < n:
            if nums[p] % 2 == 0:
                p += 2
            elif nums[q] % 2 == 1:
                q += 2
            else:
                nums[p], nums[q] = nums[q], nums[p]
                p += 2
                q += 2
        return nums

# @lc code=end

