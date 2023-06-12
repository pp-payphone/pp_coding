#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p, q = -1, n
        for i, num in enumerate(nums):
            if num <= 0:
                p = i
            if num >= 0:
                q = i
                break
        res = []
        if p == q:
            res.append(0)
            p -= 1
            q += 1
        while p != -1 or q != n:
            if p == -1 or (q != n and nums[p] + nums[q] <= 0):
                res.append(nums[q] * nums[q])
                q += 1
            else:
                res.append(nums[p] * nums[p])
                p -= 1
        return res
# @lc code=end

