#
# @lc app=leetcode.cn id=1295 lang=python3
#
# [1295] 统计位数为偶数的数字
#

# @lc code=start
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                res += 1
        return res
# @lc code=end

