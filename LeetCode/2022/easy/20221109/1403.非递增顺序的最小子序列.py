#
# @lc app=leetcode.cn id=1403 lang=python3
#
# [1403] 非递增顺序的最小子序列
#

# @lc code=start
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        sums = sum(nums)
        d = sums // 2
        res = []
        s = 0
        for each in nums:
            if s <= d:
                s += each
                res.append(each)
            else:
                break
        return res
# @lc code=end

