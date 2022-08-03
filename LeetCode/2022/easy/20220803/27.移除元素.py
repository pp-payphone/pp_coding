#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    # 和上一题类似，遍历就完事了，用自己的空间 O(n) O(1)
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        else:
            p = 0
            for q in range(n):
                if nums[q] != val:
                    nums[p] = nums[q]
                    p += 1
        return p
# @lc code=end

