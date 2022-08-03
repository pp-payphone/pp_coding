#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     """
    #     思路:遍历+看到一个删除一个
    #     时间复杂度:O(n^2)
    #     空间复杂度:O(1)
    #     """
    #     n = len(nums)
    #     if n == 0:
    #         return 0
    #     res = 1
    #     del_count = 0
    #     for i in range(1, n):
    #         if nums[i-del_count] != nums[i-del_count-1]:
    #             res += 1
    #         else:
    #             nums.pop(i-del_count)
    #             del_count += 1
    #     return res

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        思路:快指针+慢指针；不会覆盖;既然明说了不能使用额外空间，那就要好好考虑自己这个空间的利用率
        时间复杂度:O(n)
        空间复杂度:O(1)
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        slow = 0
        fast = 1
        for fast in range(1, n):
            if nums[fast] == nums[fast-1]:
                continue
            else:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1
# @lc code=end

