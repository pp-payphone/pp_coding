#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    # 最直接的思路，用一个额外hash字典保存出现过的数字，这样一次遍历后最终剩下的那个key就是只有一个的，O(n) O(n)
    # 如何使用O(1)的空间解决这个问题呢？
    # 原地冒泡排序后再遍历一遍可以不用额外空间，但是时间复杂度为O(n^2)

    # !!!!!!我想到了求和怎么就没有想到位运算啊！！！生气
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for each in nums:
            res = res ^ each
        return res
# @lc code=end

