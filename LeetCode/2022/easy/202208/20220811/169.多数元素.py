#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    # 思路一：排序之后正中间的数一定是那个多数元素
    # 时间复杂度O(n)的算法没有思路
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for each in nums:
            if count == 0:
                candidate = each
            if each == candidate:
                count += 1
            else:
                count -= 1
        return candidate
# @lc code=end

