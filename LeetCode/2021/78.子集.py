#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums):
        """
        思路：
        时间复杂度：O(n*2^n) 每个状态需要n的迭代
        空间复杂度：O(n) ；临时数组的空间
        """
        n = len(nums)
        res = [[]]
        for i in range(n):
            num = nums[i]
            res_new = [each + [num] for each in res]
            res += res_new
        return res
        
# @lc code=end

s = Solution()
res = s.subsets([1,2,3])
res