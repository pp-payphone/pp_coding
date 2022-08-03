#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        思路：
            1.左边界要比左边的大；右边界要比右边的大；
            2.右边界要在左边界右边
            ###单调栈，很有意思的思路，从高度枚举，试着自己实现一下###
        时间复杂度：
        空间复杂度：
        """
        n = len(heights)

        
# @lc code=end

