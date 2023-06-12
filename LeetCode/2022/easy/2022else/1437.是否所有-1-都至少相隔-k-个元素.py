#
# @lc app=leetcode.cn id=1437 lang=python3
#
# [1437] 是否所有 1 都至少相隔 k 个元素
#

# @lc code=start
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # min_gap = k
        # p, q = -1, -1
        # for i, each in enumerate(nums):
        #     if each == 1:
        #         p, q = q, i
        #         if p != -1:
        #             min_gap = min(min_gap, q - p - 1)
        # return min_gap >= k

        # 自己的第一个写法没有考虑提前跳出，傻了吧唧的
        n = len(nums)
        prev = -1
        for i in range(n):
            if nums[i] == 1:
                if prev != -1 and i - prev - 1 < k:
                    return False
                prev = i
        return True
# @lc code=end

