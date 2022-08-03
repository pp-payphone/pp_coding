#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        双指针，快慢
        时间复杂度:O(n)，最坏需要2*n；使用左右起始的双指针可以提升效率至最坏n，但是顺序不能保证。
        空间复杂度:O(1)
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            if nums[0] == val:
                return 0
            else:
                return 1
        slow = 0
        fast = 0
        for fast in range(n):
            if nums[fast] == val:
                continue
            else:
                nums[slow] = nums[fast]
                slow += 1
        return slow
# @lc code=end

