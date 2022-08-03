#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        思路：贪心算法做判断
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        n = len(nums)
        if n == 1:
            return True
        max_pos = 0
        for pos in range(n-1):
            max_pos = max(max_pos, pos+nums[pos])
            if max_pos == pos:
                return False
        return True

# @lc code=end

