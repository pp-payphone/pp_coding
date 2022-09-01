#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    # 后面遍历过的数往前挪用就行 O(n) O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n  == 0:
            return 0
        elif n == 1:
            return 1
        p = 0
        q = 1
        for q in range(1, n):
            if nums[p] != nums[q]:
                p += 1
                nums[p] = nums[q]
        return p + 1
# @lc code=end

