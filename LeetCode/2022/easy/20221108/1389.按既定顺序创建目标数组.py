#
# @lc app=leetcode.cn id=1389 lang=python3
#
# [1389] 按既定顺序创建目标数组
#

# @lc code=start
class Solution:
    # python可以使用insert方法效率更高
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            num, idx = nums[i], index[i]
            if idx != 0 and idx != i + 1:
                res = res[:idx] + [num] + res[idx:]
            elif idx == 0:
                res = [num] + res
            else:
                res.append(num)
        return res
# @lc code=end

