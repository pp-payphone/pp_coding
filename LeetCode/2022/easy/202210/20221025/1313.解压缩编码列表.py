#
# @lc app=leetcode.cn id=1313 lang=python3
#
# [1313] 解压缩编码列表
#

# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n // 2):
            res += [nums[2 * i + 1] for _ in range(nums[2 * i])]
        return res
# @lc code=end

