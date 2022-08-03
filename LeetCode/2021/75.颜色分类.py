#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        思路：一次扫描，0,2交换，并记录交换位置
        时间复杂度：
        空间复杂度：
        """
        n = len(nums)
        if n == 1:
            return
        l = 0
        r = n-1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[i] = nums[l]
                nums[l] = 0
                l += 1
                i = max(i, l)
            elif nums[i] == 2:
                nums[i] = nums[r]
                nums[r] = 2
                r -= 1
                # i = min(i, r)
            else:
                i += 1
        return
# @lc code=end
s = Solution()
res = s.sortColors([2,2])
res
