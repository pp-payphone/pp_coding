#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_nums = []
        for n in nums:
            if n in max_nums:
                continue
            else:
                max_nums.append(n)
                max_nums.sort(reverse=True)
                if len(max_nums) > 3:
                    max_nums.pop()
        if len(max_nums) == 3:
            return max_nums[-1]
        else:
            return max_nums[0]
            
# @lc code=end

