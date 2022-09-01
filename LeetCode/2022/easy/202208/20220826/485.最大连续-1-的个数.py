#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    # 思路：单词遍历计数
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        now = 0
        for i in nums:
            if i == 0:
                res = max(res, now)
                now = 0
            else:
                now += 1
        return max(res, now)
# @lc code=end

