#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        p = 0
        q = n - 1
        while p < q:
            if nums[p] % 2 == 0:
                p += 1
            elif nums[q] % 2 == 1:
                q -= 1
            else:
                nums[p], nums[q] = nums[q], nums[p]
                p += 1
                q -= 1
        return nums
# @lc code=end

