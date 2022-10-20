#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        flag = '='
        for i in range(n - 1):
            if nums[i + 1] == nums[i]:
                continue
            elif nums[i + 1] > nums[i]:
                if flag == '+':
                    return False
                else:
                    flag = '-'
            else:
                if flag == '-':
                    return False
                else:
                    flag = '+'
        return True

# @lc code=end

