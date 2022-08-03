#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     """
    #     思路：从左至右遍历，记录当前左侧最大连续值
    #     时间复杂度：O(N)
    #     空间复杂度：O(1)
    #     """
    #     n = len(nums)
    #     if n == 1:
    #         return nums[0]
    #     res = -1e12
    #     left_max = 0
    #     for num in nums:
    #         res = max(left_max + num, res)
    #         left_max = max(0, left_max + num)
    #     return res

    def maxSubArray(self, nums: List[int]) -> int:
        """
        思路：分治法求解
            1.随便切一刀，要么在左边中间，要么右边中间，要么左边右侧+右边左侧
        时间复杂度：O(N)
        空间复杂度：O(1)
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        def dfs(a, l, r): # 查找a列表l和r中间的最大连续子段和
            if l == r:
                return a[l]
            else:
                mid = (l+r)//2
            return
        

# @lc code=end

