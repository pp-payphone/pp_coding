#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     """
    #     遍历、笨办法
    #     时间复杂度：O(n^2)
    #     空间复杂度：O(1)
    #     """
    #     res = 0
    #     n = len(height)
    #     for l in range(n-1):
    #         for r in range(l+1, n):
    #             area = (r - l) * min(height[l], height[r])
    #             res = max(res, area)
    #     return res

    def maxArea(self, height: List[int]) -> int:
        """
        双指针遍历：向内移动长板时area一定减小
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        n = len(height)
        li = 0
        ri = n-1
        res = 0
        while ri - li > 0:
            res = max((ri - li) * min(height[li], height[ri]), res)
            if height[li] > height[ri]:
                ri -= 1
            else:
                li += 1

        
        return res
# @lc code=end

