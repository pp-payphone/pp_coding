#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 在长度 2N 的数组中找出重复 N 次的元素
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            v = m.setdefault(num, None)
            if v is not None:
                return num
            m[num] = 1
# @lc code=end

