#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
class Solution:
    # 存在优化空间，之间找最大和次大两个数就行
    def dominantIndex(self, nums: List[int]) -> int:
        n = max(nums)
        res = -1
        for idx, each in enumerate(nums):
            if each == n:
                res = idx
            elif n < each * 2:
                res = -1
                break
        return res
# @lc code=end

