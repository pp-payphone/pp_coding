#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    # def jump(self, nums) -> int:
    #     """
    #     思路：动态规划
    #     时间复杂度：O(n^2)
    #     空间复杂度：O(n)
    #     """
    #     n = len(nums)
    #     if n < 2:
    #         return 0
    #     min_steps = [0 for _ in range(n)]
    #     for i in range(n-2 , -1, -1):
    #         if nums[i] == 0:
    #             min_steps[i] = 1e12
    #         else:
    #             left_pos = min(i + nums[i] + 1, n)
    #             min_steps[i] = 1 + min(min_steps[i+1: left_pos])
    #     return min_steps[0]

    def jump(self, nums):
        """
        思路：正向贪心的去找能达到的最远距离可以更快（巧妙啊）
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        n = len(nums)
        maxPos, end, step = 0, 0, 0 # 目前最远能到的距离、
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i]) # 正向遍历的时候更新我们的最远距离
                if i == end:
                    end = maxPos
                    step += 1
        return step

# @lc code=end

s = Solution()
res = s.jump([2,3,1,1,4])
res