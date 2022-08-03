#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height) -> int:
        """
        思路：
            每列变成左侧最高与右侧侧最高中的最小值再和自身取最大值（最终高度）
            最终高度-初始高度=容量
            **使用双指针左右移动高度更低的那一侧的指针，可以将空间复杂度降低至O(1)**
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        n = len(height)
        if n < 3:
            return 0
        left_max = [0 for _ in range(n)]
        right_max = [0 for _ in range(n)]
        left_max[0] = height[0]
        right_max[n-1] = height[n-1]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i-1])
        for i in range(n-2, -1, -1):
            right_max[i] = max(height[i], right_max[i+1])
        res = 0
        for i in range(n):
            vol = max(min(left_max[i], right_max[i]), height[i]) - height[i]
            res += vol
        return res


# @lc code=end
s = Solution()
res = s.trap([4,2,0,3,2,5])
res
