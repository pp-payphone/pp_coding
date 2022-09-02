#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分
#

# @lc code=start
class Solution:
    # 逻辑题，排序之后奇数位置的数的和 O(nlogn)
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])
# @lc code=end

