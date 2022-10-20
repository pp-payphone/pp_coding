#
# @lc app=leetcode.cn id=1018 lang=python3
#
# [1018] 可被 5 整除的二进制前缀
#

# @lc code=start
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        x = 0
        for each in nums:
            x = x * 2 + each
            res.append(x % 5 == 0)
        return res
# @lc code=end

