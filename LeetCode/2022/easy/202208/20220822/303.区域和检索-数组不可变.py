#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    # 会有时间复杂度更低的算法么？

    def __init__(self, nums: List[int]):
        res = 0
        self.cum_sum = [0]
        for each in nums:
            res += each
            self.cum_sum.append(res)
        return

    def sumRange(self, left: int, right: int) -> int:
        # return sum(self.nums[left: right + 1])
        return self.cum_sum[right + 1] - self.cum_sum[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

