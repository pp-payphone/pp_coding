#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    # 思虑上肯定是有0就和后面的非0交换，但连续多个0的时候要怎么进行交换呢
    # 第一个0和第一个非0交换就行
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        i, j = -1, -1
        for p in range(n):
            if nums[p] == 0:
                if i == -1:
                    i, j = p, p
                else:
                    j = p
            else:
                if i == -1:
                    continue
                else:
                    nums[i], nums[p] = nums[p], nums[i]
                    i += 1
                    j += 1
        return

# @lc code=end

